
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_hambre_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.hambre,44)
    
  def test_Un_Zombi_sabe_correr(self):
    zombi = Zombi(44)
    self.assertTrue(zombi.sabe_correr())
    
    
  def test_Si_un_Zombi_de_hambre_100_recibe_5_puntos_de_daño_disminuye_su_hambre_en_10_puntos(self):
    zombi = Zombi(100)
    zombi.recibir_danio(5)
    self.assertEqual(zombi.hambre, 90)
    
  def test_Si_un_Zombi_recibe_mucho_danio_su_hambre_es_0(self):
    zombi = Zombi(10)
    zombi.recibir_danio(50)
    self.assertEqual(zombi.salud,0)
    
  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_hambre_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.hambre,44)
    
  def test_Un_SuperZombi_sabe_correr(self):
    superZombi = SuperZombi(44)
    self.assertTrue(superZombi.sabe_correr())

  def test_Si_un_SuperZombi_de_salud_100_recibe_20_puntos_de_daño_disminuye_su_hambre_en_20(self):
    zombi = SuperZombi(100)
    zombi.recibir_danio(20)
    self.assertEqual(zombi.hambre, 80)

    
  def test_Si_un_SuperZombi_se_regenera_su_hambre_vuelve_a_100(self):
    zombi = SuperZombi(10)
    zombi.regenerarse()
    self.assertEqual(zombi.hambre,100)
    
  def test_la_clase_SuperZombi_tiene_definido_el_método_sabe_correr(self):
    superzombi = SuperZombi(44)
    self.assertTrue("sabe_correr" in dir(superzombi) and callable(superzombi.sabe_correr))
    
  