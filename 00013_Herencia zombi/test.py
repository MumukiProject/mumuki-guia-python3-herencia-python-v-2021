
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
    
    
  def test_Si_creo_un_nuevo_super_zombi_le_puedo_especificar_su_hambre_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.hambre,44)
    

  def test_Si_un_super_zombi_de_salud_100_recibe_20_puntos_de_daño_disminuye_su_hambre_en_20(self):
    zombi = SuperZombi(100)
    zombi.recibir_danio(20)
    self.assertEqual(zombi.hambre, 80)

  def test_Si_un_super_zombi_se_regenera_su_hambre_vuelve_a_100(self):
    zombi = SuperZombi(10)
    zombi.regenerarse()
    self.assertEqual(zombi.hambre,100)
    
  def test_Un_super_zombi_siempre_es_un_peligro(self):
    gaiman = SuperZombi(0)
    self.assertTrue(gaiman.es_un_peligro())
    
  def test_Un_super_zombi_sabe_correr(self):
    superzombi = SuperZombi(44)
    self.assertTrue(superzombi.sabe_correr())
    
  def test_Un_Zombi_es_un_peligro_si_tiene_más_de_50_de_hambre(self):
    gaiman = Zombi(51)
    self.assertTrue(gaiman.es_un_peligro())
    
  def test_Un_Zombi_no_es_un_peligro_si_tiene_50_de_hambre(self):
    gaiman = Zombi(50)
    self.assertFalse(gaiman.es_un_peligro())
    
  def test_Un_Zombi_no_es_un_peligro_si_tiene_menos_de_50_de_hambre(self):
    gaiman = Zombi(49)
    self.assertFalse(gaiman.es_un_peligro())
 
  def test_Un_Zombi_no_sabe_regenerarse(self):
    caliope = Zombi(0)
    self.assertFalse("regenerarse" in dir(caliope) and callable(caliope.regenerarse))
    
  