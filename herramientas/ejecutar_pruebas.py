from pathlib import Path
import unittest,io,json,sys,hashlib
R=Path(__file__).resolve().parents[1];out=R/'validacion';out.mkdir(exist_ok=True)
suite=unittest.defaultTestLoader.discover(str(R/'herramientas'),pattern='test_*.py')
stream=io.StringIO();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
log=stream.getvalue();(out/'pruebas_modelos.txt').write_text(log,encoding='utf-8')
report={'ejecutadas':result.testsRun,'fallas':len(result.failures),'errores':len(result.errors),'omitidas':len(result.skipped),'resultado':'PASA' if result.wasSuccessful() else 'FALLA','tipo':'Pruebas funcionales con casos sintéticos; no piloto empresarial','sha256_codigo':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'herramientas').glob('*.py')}}
(out/'pruebas_modelos.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8');print(log);sys.exit(not result.wasSuccessful())
