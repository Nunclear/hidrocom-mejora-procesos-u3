"""Reglas independientes de comprobación. No modifica ni certifica datos empresariales."""
from collections import Counter,defaultdict
from decimal import Decimal
from math import sqrt,isfinite
from statistics import NormalDist

FIELDS=('cantidad','precio_unitario','subtotal_producto')
def number(x):return isinstance(x,(int,float,Decimal)) and not isinstance(x,bool) and isfinite(float(x))
def sigma_equivalente(d,total,shift=1.5):
    if not number(d) or not number(total) or d<0 or total<=0 or d>total:raise ValueError('Conteos inválidos')
    return None if d in (0,total) else NormalDist().inv_cdf(1-float(d)/float(total))+shift
def estado_principal(r):
    if r['estado_linea']=='PEDIDO' or r['estado_comprobante']=='PEDIDO':return 'Estado PEDIDO en nota o renglón'
    if any(r.get(k) is None for k in FIELDS):return 'Campos numéricos incompletos'
    if r.get('diferencia_importe') not in (None,0):return 'Diferencia de importe consignada en fuente'
    if r.get('observacion') or r.get('estado_linea')=='DUDOSA':return 'Observación o lectura dudosa documentada'
    return 'Motivo no explicitado en el detalle'
def wilson_nominal(k,n,z=1.959963984540054):
    if not isinstance(k,int) or not isinstance(n,int) or n<=0 or k<0 or k>n:raise ValueError('Conteos inválidos')
    p=k/n;den=1+z*z/n;c=(p+z*z/(2*n))/den;h=z*sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return c-h,c+h
def simulacion(revisar,objetivo,eficacia,total):
    if not all(number(x) for x in (revisar,objetivo,eficacia,total)) or total<=0 or not 0<=objetivo<=revisar<=total or not 0<=eficacia<=1:raise ValueError('Escenario inválido')
    restantes=revisar-objetivo*eficacia
    return {'eficacia_supuesta':eficacia,'revisar_esperados':restantes,'proporcion_esperada':restantes/total,'naturaleza':'Escenario; no observaciones de piloto'}
def economico(volumen_revisar_mes,fraccion_objetivo=25/38,eficacia=1,minutos_ahorrados=10,costo_hora=7.5,factor_realizable=1,costo_inicial=120,costo_recurrente_anual=0):
    vals=(volumen_revisar_mes,fraccion_objetivo,eficacia,minutos_ahorrados,costo_hora,factor_realizable,costo_inicial,costo_recurrente_anual)
    if not all(number(x) and x>=0 for x in vals) or any(x>1 for x in (fraccion_objetivo,eficacia,factor_realizable)):raise ValueError('Parámetros inválidos')
    horas=volumen_revisar_mes*fraccion_objetivo*eficacia*minutos_ahorrados/60
    bruto=horas*costo_hora*factor_realizable*12;neto=bruto-costo_inicial-costo_recurrente_anual
    unidad=fraccion_objetivo*eficacia*minutos_ahorrados/60*costo_hora*factor_realizable*12
    return {'horas_liberadas_mes':horas,'valor_anual_realizable':bruto,'neto_anual_estimado':neto,'equilibrio_revisar_mes':(costo_inicial+costo_recurrente_anual)/unidad if unidad>0 else None,'naturaleza':'Modelo con parámetros supuestos; no costo observado ni flujo de caja garantizado'}
def validar_captura(r,tolerancia=None,ids=()):
    """Oráculo del prototipo: VALIDADO significa que pasa reglas, no verdad documental."""
    fields=('id','producto','cantidad','precio','base','importe','evidencia','revisor','aprobado')
    if all(r.get(k) in (None,'') for k in fields):return 'SIN REGISTRO'
    if r.get('id') and Counter(ids)[r['id']]>1:return 'ID DUPLICADO'
    if not r.get('id') or not r.get('producto') or not all(number(r.get(k)) for k in ('cantidad','precio','base','importe')):return 'INCOMPLETO'
    if r['cantidad']<=0 or r['precio']<0 or r['base']<=0 or r['importe']<0:return 'NUMEROS INVALIDOS'
    if not number(tolerancia) or tolerancia<0:return 'DEFINIR TOLERANCIA'
    d=Decimal(str(r['importe']))-Decimal(str(r['cantidad']))*Decimal(str(r['precio']))/Decimal(str(r['base']))
    if abs(d)>Decimal(str(tolerancia)):return 'REVISAR IMPORTE'
    if not r.get('evidencia') or not r.get('revisor') or r.get('aprobado')!='SI':return 'FALTA EVIDENCIA O APROBACION'
    return 'VALIDADO'
def calculos_lote(p):
    d=p['detalle'];n=p['notas'];f=p['fechas'];N=len(d);vacios={k:sum(r[k] is None for r in d) for k in FIELDS}
    diferencias=[r for r in d if r.get('diferencia_importe') not in (None,0)]
    pendientes=[r for r in d if r['uso_importe']=='REVISAR']
    ids_pedido={r['id_detalle'] for r in pendientes if 'PEDIDO' in (r['estado_linea'],r['estado_comprobante'])}
    ids_numericos={r['id_detalle'] for r in pendientes if any(r[k] is None for k in FIELDS) or r.get('diferencia_importe') not in (None,0)}
    bynote=defaultdict(list)
    for r in d:bynote[r['id_comprobante']].append(r)
    notas_sin=sorted(set(r['id_comprobante'] for r in n)-set(bynote))
    totales=[]
    for nota in n:
        rows=bynote.get(nota['id_comprobante'],[])
        if not rows:continue
        valores=[r['subtotal_producto'] for r in rows]
        suma=sum(x for x in valores if number(x));total=nota.get('total')
        if number(total) and abs(suma-total)>.005:totales.append({'id':nota['id_comprobante'],'total_fuente':total,'suma_importes_presentes':suma,'diferencia':suma-total,'nulos_en_suma':sum(x is None for x in valores),'estado':'Discrepancia sin resolver; suma parcial si hay nulos'})
    grupos={key:[1 if r['uso_importe']=='REVISAR' else 0 for r in rows] for key,rows in bynote.items()}
    K=len(grupos);gm=len(pendientes)/N;m0=(N-sum(len(g)**2 for g in grupos.values())/N)/(K-1)
    msb=sum(len(g)*(sum(g)/len(g)-gm)**2 for g in grupos.values())/(K-1)
    msw=sum(sum((x-sum(g)/len(g))**2 for x in g) for g in grupos.values())/(N-K)
    icc=(msb-msw)/(msb+(m0-1)*msw);deff=1+(N/K-1)*icc
    escenarios=[{'D':x,'denominador_convencional':N*3,'por_millon':x/(N*3)*1e6,'sigma_equivalente':sigma_equivalente(x,N*3),'interpretacion':'Completitud sintáctica' if x==30 else 'Regla combinada hipotética; no CTQ aprobado'} for x in (30,34,35)]
    return {'notas':len(n),'renglones':N,'estados':dict(Counter(r['uso_importe'] for r in d)),'nulos_por_campo':vacios,'campos_nulos':sum(vacios.values()),'campos_inspeccionados':N*3,'renglones_con_nulos':sum(any(r[k] is None for k in FIELDS) for r in d),'diferencias_fuente':[r['id_detalle'] for r in diferencias],'escenarios_D':escenarios,'fechas_estado':dict(Counter(r.get('estado') for r in f)),'pareto_excluyente':dict(Counter(estado_principal(r) for r in pendientes)),'conjuntos':{'PEDIDO':len(ids_pedido),'numericos':len(ids_numericos),'interseccion':len(ids_pedido&ids_numericos),'union':len(ids_pedido|ids_numericos)},'caso_NP02513801':next(r for r in d if r['id_detalle']=='NP-025138-01'),'notas_sin_detalle':notas_sin,'totales_discrepantes':totales,'wilson_nominal':{'intervalo':wilson_nominal(len(pendientes),N),'supuesto':'Renglones independientes; no justifica representatividad del lote'},'agrupamiento_exploratorio':{'notas_con_detalle':K,'icc_anova_binario':icc,'efecto_diseno_aproximado':deff,'limite':'Modelo ANOVA sobre indicador binario; DEFF aproximado con tamaño medio, no diseño de muestreo confirmado'},'simulaciones':[simulacion(len(pendientes),len(ids_pedido|ids_numericos),e,N) for e in (1,.75,.5,.25)],'economia_escenarios':{'lote_mensual_supuesto':economico(38),'volumen_bajo_supuesto_13_3_meses':economico(38/13.3)}}
