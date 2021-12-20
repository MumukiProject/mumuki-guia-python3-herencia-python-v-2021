
  def test_un_auto_puede_llevar_5_personas_máximo(self):
    auto = Auto(200)
    self.assertEqual(auto.maximo_personas(),5)
    
  def test_un_auto_pierde_5_litros_de_combustible_al_recorrer_10_kilómetros(self):
    auto = Auto(200)
    auto.recorrer(10)
    self.assertEqual(auto.combustible,195)
    
  def test_un_auto_aumenta_en_20_su_combustible_al_cargarle_20_de_combustible(self):
    auto = Auto(200)
    auto.cargar_combustible(20)
    self.assertEqual(auto.combustible,220)
    
  def test_en_un_auto_entran_5_personas(self):
    auto = Auto(200)
    self.assertTrue(auto.entran_personas(5))
    
  def test_en_un_auto_entran_menos_de_5_personas(self):
    auto = Auto(200)
    self.assertTrue(auto.entran_personas(4))
    
  def test_en_un_auto_no_entran_más_de_5_personas(self):
    auto = Auto(200)
    self.assertFalse(auto.entran_personas(6))
    
  def test_una_moto_puede_llevar_2_personas_máximo(self):
    moto = Moto(100)
    self.assertEqual(moto.maximo_personas(),2)
    
  def test_una_moto_pierde_10_litros_de_combustible_al_recorrer_10_kilómetros(self):
    moto = Moto(100)
    moto.recorrer(10)
    self.assertEqual(moto.combustible,90)
    
  def test_una_moto_aumenta_en_50_su_combustible_al_cargarle_50_de_combustible(self):
    moto = Moto(100)
    moto.cargar_combustible(50)
    self.assertEqual(moto.combustible,150)
    
  def test_en_una_moto_entran_2_personas(self):
    moto = Moto(100)
    self.assertTrue(moto.entran_personas(2))
    
  def test_en_una_moto_entran_menos_de_2_personas(self):
    moto = Moto(100)
    self.assertTrue(moto.entran_personas(1))
    
  def test_en_una_moto_no_entran_más_de_2_personas(self):
    moto = Moto(100)
    self.assertFalse(moto.entran_personas(3))
    
  def test_la_clase_Auto_define_el_método_maximo_personas(self):
    auto = Auto(100)
    self.assertTrue("maximo_personas" in dir(auto) and callable(auto.maximo_personas))
    
  def test_la_clase_Moto_define_el_método_maximo_personas(self):
    moto = Moto(100)
    self.assertTrue("maximo_personas" in dir(moto) and callable(moto.maximo_personas))
    
  def test_la_clase_Auto_define_el_método_recorrer(self):
    auto = Auto(100)
    self.assertTrue("recorrer" in dir(auto) and callable(auto.recorrer))
    
  def test_la_clase_Moto_define_el_método_recorrer(self):
    moto = Moto(100)
    self.assertTrue("recorrer" in dir(moto) and callable(moto.recorrer))
    
  def test_la_clase_MedioDeTransporte_define_el_método_cargar_combustible(self):
    medioDeTransporte = MedioDeTransporte(100)
    self.assertTrue("cargar_combustible" in dir(medioDeTransporte) and callable(medioDeTransporte.cargar_combustible))
    
  def test_la_clase_MedioDeTransporte_define_el_método_entran_personas(self):
    medioDeTransporte = MedioDeTransporte(100)
    self.assertTrue("entran_personas" in dir(medioDeTransporte) and callable(medioDeTransporte.entran_personas))
    
    