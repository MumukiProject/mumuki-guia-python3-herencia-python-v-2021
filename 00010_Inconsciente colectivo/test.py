
  def test_un_colectivo_arranca_con_0_pasajeros(self):
    colectivo = Colectivo(100)
    self.assertEqual(colectivo.pasajeros,0)
    
  def test_en_un_colectivo_entran_20_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue(colectivo.entran_personas(20))
    
  def test_en_un_colectivo_entran_30_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue(colectivo.entran_personas(30))
    
  def test_en_un_colectivo_entran_35_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue(colectivo.entran_personas(35))
    
  def test_la_clase_Colectivo_define_el_método_entran_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue("entran_personas" in dir(colectivo) and callable(colectivo.entran_personas))