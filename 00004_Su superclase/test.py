
  def test_una_notebook_gasta_60_de_bateria_si_la_uso_una_hora(self):
    notebook = Notebook(100)
    notebook.utilizar(60)
    self.assertEqual(notebook.bateria,40)
    
    
  def test_una_notebook_gasta_30_de_bateria_si_lo_uso_media_hora(self):
    notebook = Notebook(100)
    notebook.utilizar(30)
    self.assertEqual(notebook.bateria,70)
    
    
  def test_una_notebook_gasta_50_de_bateria_si_lo_uso_50_minutos(self):
    notebook = Notebook(100)
    notebook.utilizar(50)
    self.assertEqual(notebook.bateria,50)

  def test_una_notebook_vuelve_a_tener_100_de_bateria_si_lo_cargo_a_tope(self):
    notebook = Notebook(100)
    notebook.utilizar(200)
    notebook.cargar_a_tope()
    self.assertEqual(notebook.bateria,100)
    
  def test_un_celular_gasta_30_de_bateria_si_lo_uso_una_hora(self):
    celular = Celular(100)
    celular.utilizar(60)
    self.assertEqual(celular.bateria,70)
    
    
  def test_un_celular_gasta_15_de_bateria_si_lo_uso_media_hora(self):
    celular = Celular(100)
    celular.utilizar(30)
    self.assertEqual(celular.bateria,85)
    
    
  def test_un_celular_gasta_25_de_bateria_si_lo_uso_50_minutos(self):
    celular = Celular(100)
    celular.utilizar(50)
    self.assertEqual(celular.bateria,75)

  def test_un_celular_vuelve_a_tener_100_de_bateria_si_lo_cargo_a_tope(self):
    celular = Celular(100)
    celular.utilizar(200)
    celular.cargar_a_tope()
    self.assertEqual(celular.bateria,100)
    
    
  def test_el_método_cargar_a_tope_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("cargar_a_tope" in dir(dispositivo) and callable(dispositivo.cargar_a_tope))
    
  def test_el_método_tiene_bateria_maxima_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("tiene_bateria_maxima" in dir(dispositivo) and callable(dispositivo.tiene_bateria_maxima))
    
  def test_el_método_cargar_a_tope_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("cargar_a_tope" in dir(dispositivo) and callable(dispositivo.cargar_a_tope))
    
  def test_el_método_utilizar_está_definido_en_la_clase_Celular(self):
    celular = Celular(1)
    self.assertTrue("utilizar" in dir(celular) and callable(celular.utilizar))
    
  def test_el_método_utilizar_está_definido_en_la_clase_Notebook(self):
    notebook = Notebook(1)
    self.assertTrue("utilizar" in dir(notebook) and callable(notebook.utilizar))
    