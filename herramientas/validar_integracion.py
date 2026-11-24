"""Validación independiente, de solo lectura sobre fuentes y entregables.

Uso: python herramientas/validar_integracion.py [--final] [--revision SHA]
Escribe resultados en validacion/. Leer cachés NO se presenta como recálculo Excel.
"""
from pathlib import Path
from collections import Counter
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from datetime import datetime,date
import argparse,json,csv,hashlib,re,sys,subprocess,platform
import openpyxl
from pypdf import PdfReader
from modelos import calculos_lote,economico,simulacion

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(value,key=''):
    if isinstance(value,(datetime,date)):return value.isoformat()[:10]
    if isinstance(value,str) and 'fecha' in str(key) and re.match(r'^\d{4}-\d{2}-\d{2}(?: |T|$)',value):return value[:10]
    return value
def sheet_rows(w,name,heads_expected):
    s=w[name];heads_expected=list(heads_expected);header_row=None
    for i,row in enumerate(s.iter_rows(min_row=1,max_row=min(12,s.max_row),values_only=True),1):
        if heads_expected[0] in row and set(heads_expected)<=set(row):header_row=i;heads=list(row);break
    if header_row is None:raise ValueError('No se encontró cabecera fuente compatible en '+name)
    out=[]
    for row in s.iter_rows(min_row=header_row+1,values_only=True):
        if row[0] is None:continue
        x=dict(zip(heads,row));out.append({k:canonical(x.get(k),k) for k in heads_expected})
    return heads,out
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');parser.add_argument('--revision',default='árbol de trabajo; ver hashes de artefactos');args=parser.parse_args()
    out=ROOT/'validacion';out.mkdir(exist_ok=True)
    checks=[];warnings=[]
    def check(name,ok,evidence):checks.append({'prueba':name,'resultado':'PASA' if ok else 'FALLA','evidencia':evidence})
    config=json.loads((ROOT/'coordinacion/contrato_datos.json').read_text(encoding='utf-8'))
    ref=ROOT/config['corte_congelado']['ruta'];check('Huella del corte congelado',sha(ref)==config['corte_congelado']['sha256'],sha(ref))
    p=json.loads(ref.read_text(encoding='utf-8'));m=calculos_lote(p)
    check('Población 73/262',m['notas']==73 and m['renglones']==262,{'notas':m['notas'],'renglones':m['renglones']})
    check('Estados 206/38/18',m['estados']==config['poblacion']['estados'],m['estados'])
    check('Identificadores de renglón únicos',len({r['id_detalle'] for r in p['detalle']})==262,'262 IDs inspeccionados')
    check('Identificadores de nota únicos',len({r['id_comprobante'] for r in p['notas']})==73,'73 IDs inspeccionados')
    check('Claves de detalle pertenecen al padrón de notas',set(r['id_comprobante'] for r in p['detalle'])<=set(r['id_comprobante'] for r in p['notas']),'Incluye notas sin detalle; no se eliminan')
    check('Completitud 5/16/9 y 786 campos',list(m['nulos_por_campo'].values())==[5,16,9] and m['campos_inspeccionados']==786,m['nulos_por_campo'])
    check('Cinco diferencias consignadas preservadas',len(m['diferencias_fuente'])==5,m['diferencias_fuente'])
    check('Incidencia millar preservada',m['caso_NP02513801']['diferencia_importe'] not in (None,0),m['caso_NP02513801'])
    check('Pareto excluyente suma 38',sum(m['pareto_excluyente'].values())==38 and sorted(m['pareto_excluyente'].values())==[5,6,7,7,13],m['pareto_excluyente'])
    check('Unión documental reproducida',m['conjuntos']=={'PEDIDO':13,'numericos':21,'interseccion':9,'union':25},m['conjuntos'])
    check('Cuatro notas sin detalle visibles',len(m['notas_sin_detalle'])==4,m['notas_sin_detalle'])
    check('Diez diferencias de total identificadas',len(m['totales_discrepantes'])==10,{'cantidad':len(m['totales_discrepantes']),'no_se_corrigen':True})
    check('D30 conversión independiente',abs(m['escenarios_D'][0]['por_millon']-38167.938931297715)<1e-8 and abs(m['escenarios_D'][0]['sigma_equivalente']-3.27235360650087)<1e-10,m['escenarios_D'][0])
    check('Extremos de simulación',abs(m['simulaciones'][0]['proporcion_esperada']-13/262)<1e-12 and abs(m['simulaciones'][3]['proporcion_esperada']-31.75/262)<1e-12,m['simulaciones'])
    econ=m['economia_escenarios'];check('Modelo económico 255 / negativo / equilibrio',abs(econ['lote_mensual_supuesto']['neto_anual_estimado']-255)<1e-9 and round(econ['volumen_bajo_supuesto_13_3_meses']['neto_anual_estimado'],2)==-91.8 and abs(econ['lote_mensual_supuesto']['equilibrio_revisar_mes']-12.16)<1e-9,econ)
    books=[];manifest=[];pdfs=[];ooxml=[]
    for f in sorted(ROOT.rglob('*')):
        if not f.is_file() or any(x in {'.git','.qa','__pycache__','auditoria_integral','validacion','datos_control','coordinacion'} for x in f.relative_to(ROOT).parts):continue
        rel=f.relative_to(ROOT).as_posix()
        if f.suffix.lower() in ('.xlsx','.docx','.pptx','.pdf'):
            manifest.append({'archivo':rel,'sha256':sha(f),'bytes':f.stat().st_size})
        if f.suffix.lower()=='.xlsx':
            try:
                wf=openpyxl.load_workbook(f,data_only=False,read_only=False);wv=openpyxl.load_workbook(f,data_only=True,read_only=True)
                formula_count=0;missing=[];errors=[];validations=0
                empty_strings={}
                with ZipFile(f) as z:
                    n={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                    rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'));targets={x.attrib['Id']:x.attrib['Target'] for x in rels}
                    bookxml=ET.fromstring(z.read('xl/workbook.xml'))
                    for sn in bookxml.findall('.//s:sheet',n):
                        rid=sn.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'];target=targets[rid]
                        target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
                        sx=ET.fromstring(z.read(target));empty_strings[sn.attrib['name']]={x.attrib['r'] for x in sx.findall('.//s:c',n) if x.attrib.get('t')=='str' and x.find('s:f',n) is not None and x.find('s:v',n) is not None and x.find('s:v',n).text in (None,'')}
                for s in wf:
                    validations+=len(s.data_validations.dataValidation)
                    for row in s:
                        for cell in row:
                            if cell.data_type=='f':
                                formula_count+=1
                                # Read-only .cell would reparse XML for every access. Cache once below.
                    sv=wv[s.title]
                    cached={c.coordinate:c for row in sv for c in row if hasattr(c,'coordinate')}
                    for row in s:
                        for cell in row:
                            v=cached.get(cell.coordinate)
                            if cell.data_type=='f' and (v is None or v.value is None) and cell.coordinate not in empty_strings.get(s.title,set()):missing.append(s.title+'!'+cell.coordinate)
                            if v is not None and v.data_type=='e':errors.append({'celda':s.title+'!'+cell.coordinate,'error':v.value})
                check('Caché sin errores Excel: '+rel,not errors,errors)
                if missing:warnings.append({'archivo':rel,'tipo':'Fórmulas sin caché; exige motor de cálculo','celdas':missing})
                if 'Datos' in wf.sheetnames:
                    heads,rows=sheet_rows(wf,'Datos',p['detalle'][0].keys());expected=p['detalle'];diff=[]
                    for i,(a,b) in enumerate(zip(rows,expected),6):
                        for key in b:
                            if a[key]!=b[key]:diff.append({'fila':i,'campo':key,'actual':a[key],'referencia':b[key]})
                    check('Fuente Datos preservada: '+rel,len(rows)==len(expected) and not diff,{'filas':len(rows),'celdas_comparadas':len(rows)*len(expected[0]),'diferencias':diff[:20]})
                if rel.startswith('03_DMAIC/'):
                    for name,key in [('Comprobantes','notas'),('Fechas','fechas')]:
                        if name not in wf.sheetnames:check('Fuente '+name+' existe: '+rel,False,'Hoja ausente');continue
                        _,rows=sheet_rows(wf,name,p[key][0].keys());check('Fuente '+name+' preservada: '+rel,rows==p[key],{'filas':len(rows)})
                with ZipFile(f) as z:
                    external=[x for x in z.namelist() if x.startswith('xl/externalLinks/')]
                    check('Sin dependencia de otro libro: '+rel,not external,external)
                books.append({'archivo':rel,'hojas':wf.sheetnames,'formulas_inspeccionadas':formula_count,'formulas_sin_cache':len(missing),'validaciones_de_datos':validations,'errores_cache':len(errors),'motor_ejecutado_por_este_script':False})
                wf.close();wv.close()
            except Exception as ex:check('Apertura Excel: '+rel,False,str(ex))
        elif f.suffix.lower()=='.pdf':
            try:
                d=PdfReader(f);texts=[x.extract_text() or '' for x in d.pages]
                check('PDF abre y tiene texto: '+rel,bool(texts) and all(t.strip() for t in texts),{'paginas':len(texts),'revision_visual':'Requiere evidencia adicional; esta prueba solo extrae texto'})
                pdfs.append({'archivo':rel,'paginas':len(texts)})
                dest=out/'texto_pdf';dest.mkdir(exist_ok=True);(dest/(f.stem+'.txt')).write_text('\n\n'.join(texts),encoding='utf-8')
            except Exception as ex:check('Apertura PDF: '+rel,False,str(ex))
        elif f.suffix.lower() in ('.docx','.pptx'):
            try:
                with ZipFile(f) as z:
                    bad=z.testzip();xmls=[x for x in z.namelist() if x.endswith('.xml')]
                    for x in xmls:ET.fromstring(z.read(x))
                    slides=[x for x in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',x)]
                    check('Integridad OOXML: '+rel,bad is None,{'xml':len(xmls),'slides':len(slides),'limite':'No es revisión visual'})
                    ooxml.append({'archivo':rel,'xml':len(xmls),'diapositivas':len(slides),'revision_visual_pendiente':True})
            except Exception as ex:check('Integridad OOXML: '+rel,False,str(ex))
    for folder in ['01_Lean','02_Seis_Sigma','03_DMAIC']:
        for ext in ['docx','pdf','xlsx','pptx']:
            present=any((ROOT/folder).glob('*.'+ext))
            if args.final:check('Entrega independiente '+folder+' / '+ext,present,'Exige al menos un archivo')
            elif not present:warnings.append({'archivo':folder,'tipo':'Entregable aún pendiente','extension':ext})
    # Inspect local Markdown links. External links require their own permissions and are not claimed tested.
    links=[]
    for md in ROOT.rglob('*.md'):
        if any(x in {'.git','.qa'} for x in md.parts):continue
        text=md.read_text(encoding='utf-8-sig')
        for target in re.findall(r'\]\(([^)\n]+)\)',text):
            t=target.strip('<> ')
            if t.startswith(('http:','https:','mailto:','#')) or '"' in t:continue
            path=(md.parent/t.split('#')[0]).resolve()
            if not path.exists():links.append({'archivo':md.relative_to(ROOT).as_posix(),'enlace':t})
    check('Enlaces Markdown locales resolubles',not links,links)
    report={'revision_declarada':args.revision,'python':platform.python_version(),'openpyxl':openpyxl.__version__,'tipo':'Cálculo Python y revisión estructural/cachés; no recálculo Excel ni render visual','modo_final':args.final,'metricas':m,'pruebas':checks,'avisos':warnings,'libros':books,'pdfs':pdfs,'ooxml':ooxml,'artefactos':manifest,'resumen':{'pasan':sum(x['resultado']=='PASA' for x in checks),'fallan':sum(x['resultado']=='FALLA' for x in checks),'avisos':len(warnings),'formulas_inspeccionadas':sum(x['formulas_inspeccionadas'] for x in books)}}
    (out/'resultados_integracion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
    with (out/'MANIFIESTO_ARTEFACTOS.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['archivo','sha256','bytes']);w.writeheader();w.writerows(manifest)
    print(json.dumps(report['resumen'],ensure_ascii=False));return bool(report['resumen']['fallan'])
if __name__=='__main__':sys.stdout.reconfigure(encoding='utf-8');sys.exit(main())
