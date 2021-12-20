
  def test_un_colectivo_carga_50_de_combustible_cuando_le_cargamos_50_litros_de_combustible(self):
    colectivo = Colectivo()
    colectivo.cargar_combustible(50)
    self.assertEqual(colectivo.combustible,150)
    
  def test_un_colectivo_pierde_sus_pasajeros_al_cargar_combustible(self):
    colectivo = Colectivo()
    colectivo.cargar_pasajeros(100)
    colectivo.cargar_combustible(50)
    self.assertEqual(colectivo.pasajeros,0)
  
  def test_la_clase_Colectivo_define_el_método_cargar_combustible(self):
    colectivo = Colectivo(100)
    self.assertTrue("cargar_combustible" in dir(colectivo) and callable(colectivo.cargar_combustible))
    
    
# Seguro hay alguna manera de definir cargar_pasajeros en el extra code, pero no pude hacerlo, habría que evaluar si se lo pedimos o lo agregamos
#def cargar_pasajeros(self,cant_pasajeros):
#    self.pasajeros += cant_pasajeros