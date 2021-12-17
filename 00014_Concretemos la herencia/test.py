
  def test_El_método_descansar_está_definido_en_la_clase_Zombi(self):
    zombi = Zombi(44)
    self.assertTrue("descansar" in dir(zombi) and callable(zombi.descansar))
    
    
  def test_Cuando_un_Zombi_descansa_una_cantidad_de_minutos_restaura_su_salud_en_esa_cantidad(self):
    zombi = Zombi(44)
    zombi.descansar(56)
    self.assertEqual(zombi.salud, 100) 
    
  def test_Cuando_un_SuperZombi_descansa_una_cantidad_de_minutos_restaura_su_salud_en_esa_cantidad(self):
    zombi = SuperZombi(44)
    zombi.descansar(56)
    self.assertEqual(zombi.salud, 100) 