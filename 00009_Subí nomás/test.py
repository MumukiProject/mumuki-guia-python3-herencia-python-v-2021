
  def test_un_colectivo_puede_llevar_20_personas_máximo(self):
    colectivo = Colectivo(300)
    self.assertEqual(colectivo.maximo_personas(),20)
    
  def test_un_colectivo_pierde_20_litros_de_combustible_al_recorrer_10_kilómetros(self):
    colectivo = Colectivo(300)
    colectivo.recorrer(10)
    self.assertEqual(colectivo.combustible,280)
    
  def test_un_colectivo_aumenta_en_20_su_combustible_al_cargarle_20_de_combustible(self):
    colectivo = Colectivo(300)
    colectivo.cargar_combustible(20)
    self.assertEqual(colectivo.combustible,320)
    
  def test_en_un_auto_entran_20_personas(self):
    colectivo = Colectivo(300)
    self.assertTrue(colectivo.entran_personas(20))
    
  def test_en_un_colectivo_entran_menos_de_20_personas(self):
    colectivo = Colectivo(300)
    self.assertTrue(colectivo.entran_personas(19))
    
  def test_en_un_auto_no_entran_más_de_20_personas(self):
    colectivo = Colectivo(300)
    self.assertFalse(colectivo.entran_personas(21))
    
  def test_la_clase_Colectivo_define_el_método_recorrer(self):
    colectivo = Colectivo(100)
    self.assertTrue("recorrer" in dir(colectivo) and callable(colectivo.recorrer))
    
  def test_la_clase_Colectivo_define_el_método_maximo_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue("maximo_personas" in dir(colectivo) and callable(colectivo.maximo_personas))