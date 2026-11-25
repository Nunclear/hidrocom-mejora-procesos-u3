import unittest,math
from modelos import sigma_equivalente,wilson_nominal,simulacion,economico,validar_captura,estado_principal

class ModelosTest(unittest.TestCase):
    def test_sigma_vacios_y_extremos(self):
        self.assertAlmostEqual(sigma_equivalente(30,786),3.27235360650087)
        self.assertIsNone(sigma_equivalente(0,786));self.assertIsNone(sigma_equivalente(786,786))
        for a,b in [(-1,786),(787,786),(1,0)]:
            with self.assertRaises(ValueError):sigma_equivalente(a,b)
    def test_simulacion_no_observacion(self):
        self.assertAlmostEqual(simulacion(38,25,1,262)['proporcion_esperada'],13/262)
        self.assertAlmostEqual(simulacion(38,25,.25,262)['revisar_esperados'],31.75)
        self.assertEqual(simulacion(38,25,0,262)['revisar_esperados'],38)
        with self.assertRaises(ValueError):simulacion(38,39,1,262)
    def test_economia_sensibilidad(self):
        self.assertAlmostEqual(economico(38)['neto_anual_estimado'],255)
        self.assertAlmostEqual(economico(38/13.3)['neto_anual_estimado'],-91.80451127819549)
        self.assertAlmostEqual(economico(38)['equilibrio_revisar_mes'],12.16)
        self.assertEqual(economico(38,eficacia=0)['neto_anual_estimado'],-120)
        self.assertIsNone(economico(38,eficacia=0)['equilibrio_revisar_mes'])
        self.assertAlmostEqual(economico(38,costo_recurrente_anual=100)['neto_anual_estimado'],155)
        self.assertAlmostEqual(economico(38,factor_realizable=.5)['neto_anual_estimado'],67.5)
        for kwargs in [{'volumen_revisar_mes':-1},{'volumen_revisar_mes':38,'eficacia':1.1},{'volumen_revisar_mes':38,'costo_hora':float('nan')}]:
            with self.assertRaises(ValueError):economico(**kwargs)
    def test_wilson_nominal(self):
        lo,hi=wilson_nominal(38,262);self.assertAlmostEqual(lo,.10753,places=4);self.assertAlmostEqual(hi,.19281,places=4)
    def test_captura_no_basta_solo_importe(self):
        r={'id':'QA-ONLY','producto':'Ejemplo sintético','cantidad':2,'precio':5,'base':1,'importe':10,'evidencia':'QA','revisor':'QA','aprobado':'SI'}
        self.assertEqual(validar_captura(r,0),'VALIDADO')
        self.assertEqual(validar_captura({**r,'precio':None},0),'INCOMPLETO')
        self.assertEqual(validar_captura({**r,'evidencia':None},0),'FALTA EVIDENCIA O APROBACION')
        self.assertEqual(validar_captura({**r,'base':0},0),'NUMEROS INVALIDOS')
        self.assertEqual(validar_captura({**r,'importe':11},0),'REVISAR IMPORTE')
        self.assertEqual(validar_captura(r,None),'DEFINIR TOLERANCIA')
        self.assertEqual(validar_captura(r,0,ids=['QA-ONLY','QA-ONLY']),'ID DUPLICADO')
        self.assertEqual(validar_captura({},0),'SIN REGISTRO')
    def test_base_millar_solo_sintetica(self):
        r={'id':'QA-MILLAR','producto':'Caso sintético con base explícita','cantidad':2000,'precio':240,'base':1000,'importe':480,'evidencia':'QA','revisor':'QA','aprobado':'SI'}
        self.assertEqual(validar_captura(r,0),'VALIDADO')
    def test_prioridad_pareto_no_duplica(self):
        r={'estado_linea':'PEDIDO','estado_comprobante':'SIN_MARCA','cantidad':None,'precio_unitario':None,'subtotal_producto':None,'diferencia_importe':99,'observacion':'Duda'}
        self.assertEqual(estado_principal(r),'Estado PEDIDO en nota o renglón')

if __name__=='__main__':unittest.main()
