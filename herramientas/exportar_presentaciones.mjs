// Local fallback after three Artifact Session PPTX export host failures.
// Uses the same callback/data already authored and reviewed in the session.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {buildBatch,specs} from './crear_presentaciones.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const resolver=createRequire(path.join(process.env.HIDROCOM_NODE_MODULES,'__hidrocom_loader__.cjs'));
const {FileBlob,PresentationFile}=await import(pathToFileURL(resolver.resolve('@oai/artifact-tool')).href);
const skill=process.env.HIDROCOM_PRESENTATIONS_SKILL;
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const qa=path.join(root,'.qa/presentaciones');await fs.mkdir(qa,{recursive:true});
const original=path.join(root,'04_Producto_Final/U3_Presentacion_HIDROCOM.pptx');
const starter=path.join(qa,'template-starter.pptx');
try{await fs.access(starter);}catch{await fs.copyFile(path.join(root,'documentacion/plantillas/Presentacion_U3_base.pptx'),starter);}
const refhash=createHash('sha256').update(await fs.readFile(starter)).digest('hex');
const mappings={dmaic:['03_DMAIC','U3_DMAIC_HIDROCOM'],lean:['01_Lean','U3_Lean_HIDROCOM'],sigma:['02_Seis_Sigma','U3_Seis_Sigma_HIDROCOM']};
const receipts=[];
for(const kind of (process.argv.slice(2).length?process.argv.slice(2):Object.keys(mappings))){
 const p=await PresentationFile.importPptx(await FileBlob.load(starter));
 const result=await p.inspect({select:'$.slides[0].elements[*]',include:['id','text']});
 const replacements=[['PROYECTO LEAN SEIS SIGMA','PROYECTO '+(kind==='sigma'?'SEIS SIGMA':kind.toUpperCase())+' · UNIDAD 3'],['Menos renglones','Registro y validación\ndocumental trazable'],['GRUPO HIDROCOM','GRUPO HIDROCOM KALLPA E.I.R.L.\nLote académico: 73 notas · 262 renglones'],['Champion:','Integrantes registrados en el manual:\nGutierrez Morales Jhon Alex\nMullisaca Condori Carlos Augusto\nMamani Mamani Ciro Wagner\nRoles Champion / BB / GB: pendientes'],['Mejora de Procesos','Mejora de Procesos y Calidad Total · U3\nCorte de revisión: 24/11/2026']];
 for(const [prefix,text] of replacements){const hit=result.records.find(r=>String(r.text||'').includes(prefix));if(!hit)throw Error('Cover shape not found: '+prefix);p.resolve(hit.id).text=text;}
 p.slides.getItem(0).speakerNotes.text='Portada y marca de la plantilla suministrada. Equipo registrado en el manual; sin asignación de roles ni certificación. Origen y fecha reportada sin verificar.';
 for(let start=0;start<specs[kind].length;start+=4)await buildBatch({presentation:p,input:{kind,start,count:4}});
 for(const s of p.slides.items)for(const ch of s.charts.items)applyPresentationChartFont(ch,{fontFamily:'Calibri'});
 const dir=path.join(qa,kind);await fs.mkdir(dir,{recursive:true});
 for(let i=0;i<p.slides.items.length;i++){await fs.writeFile(path.join(dir,`slide-${i+1}.png`),new Uint8Array(await (await p.export({format:'png',slide:p.slides.getItem(i),scale:1})).arrayBuffer()));const l=await p.slides.getItem(i).export({format:'layout'});await fs.writeFile(path.join(dir,`slide-${i+1}.layout.json`),await l.text());}
 const candidate=path.join(dir,'candidate.pptx');await (await PresentationFile.exportPptx(p)).save(candidate);
 const finalDir=path.join(qa,'finales',kind);await fs.mkdir(finalDir,{recursive:true});const final=path.join(finalDir,'final.pptx');
 const finalization=await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.HIDROCOM_PYTHON,integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','9144000,5143500','--validate-bullet-geometry','--validate-heading-fit',...specs[kind].flatMap((s,i)=>s.rows?['--require-native-table-slide',String(i+2)]:[])],explicitTotalSlideCount:specs[kind].length+1,requiredNativeTableOwnerSlides:specs[kind].map((s,i)=>s.rows?i+2:null).filter(Boolean),requiredNativeChartOwnerSlides:specs[kind].map((s,i)=>s.chart?i+2:null).filter(Boolean),materializeLiteralChartWorkbooks:true,fontPolicy:{basis:'reference',families:['Calibri'],referencePath:starter,referenceSha256:refhash},verifyArtifactToolImport:true,receiptPath:path.join(dir,'finalization.json')});
 const [folder,stem]=mappings[kind];await fs.copyFile(final,path.join(root,folder,stem+'.pptx'));if(kind==='dmaic')await fs.copyFile(final,original);
 receipts.push({kind,slides:p.slides.items.length,sha256:createHash('sha256').update(await fs.readFile(final)).digest('hex'),file:folder+'/'+stem+'.pptx',finalization});
 console.log(JSON.stringify({kind,slides:p.slides.items.length,status:'exported'}));
}
await fs.writeFile(path.join(root,'validacion/presentaciones_exportacion.json'),JSON.stringify({method:'Artifact Tool local fallback; export host failed three times; native tables, charts and process diagrams',referenceSha256:refhash,receipts},null,2));
