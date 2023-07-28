  
  def test_un_colectivo_arranca_con_100_de_combustible(self):
    colectivo = Colectivo(100)
    self.assertEqual(colectivo.combustible,100)
    
  def test_un_colectivo_arranca_con_0_pasajeros(self):
    colectivo = Colectivo(100)
    self.assertEqual(colectivo.pasajeros,0)
    
  def test_en_un_colectivo_entran_20_personas(self):
    colectivo = Colectivo(100)
    self.assertTrue(colectivo.entran_personas(20))
    
  def test_un_colectivo_carga_50_de_combustible_cuando_le_cargamos_50_litros_de_combustible(self):
    colectivo = Colectivo(100)
    colectivo.cargar_combustible(50)
    self.assertEqual(colectivo.combustible,150)
    
  def test_un_colectivo_pierde_sus_pasajeros_al_cargar_combustible(self):
    colectivo = Colectivo(100)
    colectivo.pasajeros = 100
    colectivo.cargar_combustible(50)
    self.assertEqual(colectivo.pasajeros,0)