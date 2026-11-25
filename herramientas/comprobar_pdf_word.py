"""Inspecciona exportaciones PDF realizadas desde Word por la interfaz nativa.
No automatiza Office. Renderiza todas las páginas con PDFium y registra huellas.
"""
from pathlib import Path
import json,hashlib,re
from pypdf import PdfReader
import pypdfium2 as pdfium
from docx import Document
R=Path(__file__).resolve().parents[1];qa=R/'.qa/word';results=[]
for folder,stem in [('01_Lean','U3_Lean_HIDROCOM'),('02_Seis_Sigma','U3_Seis_Sigma_HIDROCOM'),('03_DMAIC','U3_DMAIC_HIDROCOM')]:
    f=qa/(stem+'.pdf');docx=R/folder/(stem+'.docx');reader=PdfReader(f);pdf=pdfium.PdfDocument(f);dest=qa/(stem+'_paginas');dest.mkdir(exist_ok=True)
    pages=[]
    for i,p in enumerate(pdf):
        p.render(scale=1.15).to_pil().save(dest/f'pagina-{i+1:02}.png');text=reader.pages[i].extract_text() or '';pages.append({'pagina':i+1,'caracteres':len(text),'texto_no_vacio':bool(text.strip())})
    text='\n'.join(p.extract_text() or '' for p in reader.pages)
    (qa/(stem+'.txt')).write_text(text,encoding='utf8')
    # All informative DOCX tokens should survive PDF export; punctuation/hyphenation normalized.
    d=Document(docx);raw=' '.join([p.text for p in d.paragraphs]+[c.text for t in d.tables for row in t.rows for c in row.cells]);norm=lambda t:re.sub(r'[^\w]+','',t).casefold()
    tokens=set(re.findall(r'[A-Za-zÁÉÍÓÚáéíóúñÑ0-9]{5,}',raw));missing=sorted(t for t in tokens if norm(t) not in norm(text))
    results.append({'docx':folder+'/'+stem+'.docx','pdf':folder+'/'+stem+'.pdf','pdf_origen':'Exportación en Microsoft Word por interfaz local','sha256_docx':hashlib.sha256(docx.read_bytes()).hexdigest(),'sha256_pdf':hashlib.sha256(f.read_bytes()).hexdigest(),'paginas':pages,'tokens_largos_ausentes':missing,'revision_visual':'Pendiente; imágenes generadas para inspección de A'})
(R/'validacion/pdf_word.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'pdf':x['pdf'],'paginas':len(x['paginas']),'tokens_ausentes':x['tokens_largos_ausentes']} for x in results],ensure_ascii=False))
