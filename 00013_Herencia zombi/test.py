
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_salud_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.salud,44)
    
  def test_Un_Zombi_no_sabe_correr(self):
    zombi = Zombi(44)
    self.assertFalse(zombi.sabe_correr())
    
  def test_Un_Zombi_sabe_gritar(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.gritar(),'¡agrrrg!')
    
  def test_Un_Zombi_con_vida_100_no_está_sin_vida(self):
    zombi = Zombi(100)
    self.assertFalse(zombi.sin_vida())
    
  def test_Si_un_Zombi_de_salud_100_recibe_5_puntos_de_daño_disminuye_su_salud_en_10_puntos_y_no_está_sin_vida(self):
    zombi = Zombi(100)
    zombi.recibir_danio(5)
    self.assertFalse(zombi.sin_vida())
    
  def test_Si_un_Zombi_recibe_mucho_danio_su_salud_es_0_y_está_sin_vida(self):
    zombi = Zombi(10)
    zombi.recibir_danio(50)
    self.assertEqual(zombi.salud,0)
    self.assertTrue(zombi.sin_vida())
    
  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_salud_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.salud,44)
    
  def test_Un_SuperZombi_sabe_correr(self):
    superZombi = SuperZombi(44)
    self.assertTrue(superZombi.sabe_correr())
    
  def test_Un_SuperZombi_sabe_gritar(self):
    zombi = SuperZombi(44)
    self.assertEqual(zombi.gritar(),'¡agrrrg!')
    
  def test_Un_SuperZombi_con_vida_100_no_está_sin_vida(self):
    zombi = SuperZombi(100)
    self.assertFalse(zombi.sin_vida())  
    
  def test_Si_un_SuperZombi_de_salud_100_recibe_5_puntos_de_daño_disminuye_su_salud_en_15_puntos_y_no_está_sin_vida(self):
    zombi = SuperZombi(100)
    zombi.recibir_danio(5)
    self.assertEqual(zombi.salud, 85)
    self.assertFalse(zombi.sin_vida())
    
  def test_Si_un_SuperZombi_recibe_mucho_danio_su_salud_es_0_y_está_sin_vida(self):
    zombi = SuperZombi(10)
    zombi.recibir_danio(50)
    self.assertEqual(zombi.salud,0)
    self.assertTrue(zombi.sin_vida())
    
  def test_Si_un_SuperZombi_se_regenera_su_salud_vuelve_a_100(self):
    zombi = SuperZombi(10)
    zombi.regenerarse()
    self.assertEqual(zombi.salud,100)
    
  def test_la_clase_SuperZombi_tiene_definido_el_método_sabe_correr(self):
    superzombi = SuperZombi(44)
    self.assertTrue("sabe_correr" in dir(superzombi) and callable(superzombi.sabe_correr))
    
    
  def test_la_clase_SuperZombi_tiene_definido_el_método_recibir_danio(self):
    superzombi = SuperZombi(44)
    self.assertTrue("regenarse" in dir(superzombi) and callable(superzombi.regenerarse))
  