
  def test_Si_creo_un_nuevo_Zombi_le_puedo_especificar_su_hambre_inicial(self):
    zombi = Zombi(44)
    self.assertEqual(zombi.hambre,44)

  def test_Si_creo_un_nuevo_SuperZombi_le_puedo_especificar_su_hambre_inicial(self):
    superZombi = SuperZombi(44)
    self.assertEqual(superZombi.hambre,44)
    
  def test_Un_super_zombi_sabe_correr(self):
    gaiman = SuperZombi(100)
    self.assertTrue(gaiman.sabe_correr())
    
  def test_Un_super_zombi_pasa_a_tener_100_de_hambre_al_regenerarse(self):
    gaiman = SuperZombi(0)
    gaiman.regenerarse()
    self.assertEqual(gaiman.hambre, 100)
    
  def test_Si_un_super_zombi_con_hambre_100_recibe_20_de_danio_su_hambre_queda_en_80(self):
    gaiman = SuperZombi(100)
    gaiman.recibir_danio(20)
    self.assertEqual(gaiman.hambre, 80)
    
  def test_Si_un_super_zombi_con_hambre_50_recibe_10_de_danio_su_hambre_queda_en_40(self):
    gaiman = SuperZombi(50)
    gaiman.recibir_danio(10)
    self.assertEqual(gaiman.hambre, 40)
    
  def test_Un_super_zombi_siempre_es_un_peligro(self):
    gaiman = SuperZombi(0)
    self.assertTrue(gaiman.es_un_peligro())
    
  def test_Un_zombi_sabe_correr(self):
    gaiman = Zombi(100)
    self.assertTrue(gaiman.sabe_correr())
    
  def test_Si_un_zombi_con_hambre_80_recibe_10_de_danio_su_hambre_queda_en_60(self):
    gaiman = Zombi(80)
    gaiman.recibir_danio(10)
    self.assertEqual(gaiman.hambre, 60)
    
  def test_Si_un_zombi_con_hambre_70_recibe_15_de_danio_su_hambre_queda_en_40(self):
    gaiman = Zombi(70)
    gaiman.recibir_danio(15)
    self.assertEqual(gaiman.hambre, 40)
    
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
    
  def test_El_método_sabe_correr_está_definido_en_la_clase_zombi(self):
    caliope = Zombi(0)
    self.assertTrue("sabe_correr" in dir(caliope) and callable(caliope.sabe_correr))
    
  def test_El_método_recibir_danio_está_definido_en_la_clase_zombi(self):
    caliope = Zombi(0)
    self.assertTrue("recibir_danio" in dir(caliope) and callable(caliope.recibir_danio))
    
  def test_El_método_recibir_danio_está_definido_en_la_clase_SuperZombi(self):
    caliope = SuperZombi(0)
    self.assertTrue("recibir_danio" in dir(caliope) and callable(caliope.recibir_danio))
    
  def test_El_método_es_un_peligro_está_definido_en_la_clase_zombi(self):
    caliope = Zombi(0)
    self.assertTrue("es_un_peligro" in dir(caliope) and callable(caliope.es_un_peligro))
    
  def test_El_método_es_un_peligro_está_definido_en_la_clase_SuperZombi(self):
    caliope = SuperZombi(0)
    self.assertTrue("es_un_peligro" in dir(caliope) and callable(caliope.es_un_peligro))