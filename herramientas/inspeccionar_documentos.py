"""Extrae texto y medios para revisión independiente. No valida el render visual."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json,hashlib,sys,re
R=Path(__file__).resolve().parents[1];out=R/'validacion'/'documentos';out.mkdir(exist_ok=True)
results=[]
for p in sorted(R.rglob('*.docx')):
    if any(x in {'.git','.qa','auditoria_integral'} for x in p.parts):continue
    with ZipFile(p) as z:
        root=ET.fromstring(z.read('word/document.xml'));ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        pars=[''.join(t.text or '' for t in x.findall('.//w:t',ns)) for x in root.findall('.//w:p',ns)]
        text='\n'.join(pars);(out/(p.stem+'.txt')).write_text(text,encoding='utf-8')
        media=[];dest=R/'.qa'/'word'/p.stem;dest.mkdir(parents=True,exist_ok=True)
        for n in z.namelist():
            if n.startswith('word/media/'):
                b=z.read(n);(dest/Path(n).name).write_bytes(b);sha=hashlib.sha256(b).hexdigest()
                media.append({'media':n,'sha256':sha,'coincide_png_actual':[x.relative_to(R).as_posix() for x in (R/'04_Producto_Final').glob('*.png') if hashlib.sha256(x.read_bytes()).hexdigest()==sha]})
        rows=[t for t in pars if any(s in t.lower() for s in ['juliaca','meta','3,27','3.27','causa','primera','pm-08','255','91,8','9 %','champion'])]
        results.append({'archivo':p.relative_to(R).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'parrafos':len(pars),'medios':media,'texto_para_cotejo':rows,'revision_visual':'Pendiente de render y lectura de todas las páginas'})
(out/'inspeccion_ooxml.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8');print(json.dumps(results,ensure_ascii=False,indent=2))
