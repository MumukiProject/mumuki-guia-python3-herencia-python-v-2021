
  def test_Una_notebook_gasta_60_de_bateria_si_la_uso_una_hora(self):
    notebook = Notebook(100)
    notebook.utilizar(60)
    self.assertEqual(notebook.bateria,40)
    
    
  def test_Una_notebook_gasta_30_de_bateria_si_lo_uso_media_hora(self):
    notebook = Notebook(100)
    notebook.utilizar(30)
    self.assertEqual(notebook.bateria,70)
    
    
  def test_Una_notebook_gasta_50_de_bateria_si_lo_uso_50_minutos(self):
    notebook = Notebook(100)
    notebook.utilizar(50)
    self.assertEqual(notebook.bateria,50)

  def test_Una_notebook_vuelve_a_tener_100_de_bateria_si_lo_cargo_a_tope(self):
    notebook = Notebook(100)
    notebook.utilizar(200)
    notebook.cargar_a_tope()
    self.assertEqual(notebook.bateria,100)
    
  def test_Una_tablet_gasta_30_de_bateria_si_lo_uso_una_hora(self):
    tablet = Tablet(100)
    tablet.utilizar(60)
    self.assertEqual(tablet.bateria,70)
    
    
  def test_Una_tablet_gasta_15_de_bateria_si_la_uso_media_hora(self):
    tablet = Tablet(100)
    tablet.utilizar(30)
    self.assertEqual(tablet.bateria,85)
    
    
  def test_Una_tablet_gasta_25_de_bateria_si_la_uso_50_minutos(self):
    tablet = Tablet(100)
    tablet.utilizar(50)
    self.assertEqual(tablet.bateria,75)

  def test_Una_tablet_vuelve_a_tener_100_de_bateria_si_la_cargo_a_tope(self):
    tablet = Tablet(100)
    tablet.utilizar(200)
    tablet.cargar_a_tope()
    self.assertEqual(tablet.bateria,100)
    
    
  def test_el_método_cargar_a_tope_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("cargar_a_tope" in dir(dispositivo) and callable(dispositivo.cargar_a_tope))
    
  def test_el_método_tiene_bateria_maxima_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("tiene_bateria_maxima" in dir(dispositivo) and callable(dispositivo.tiene_bateria_maxima))
    
  def test_el_método_cargar_a_tope_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("cargar_a_tope" in dir(dispositivo) and callable(dispositivo.cargar_a_tope))
    
  def test_el_método_utilizar_está_definido_en_la_clase_Tablet(self):
    tablet = Tablet(1)
    self.assertTrue("utilizar" in dir(tablet) and callable(tablet.utilizar))
    
  def test_el_método_utilizar_está_definido_en_la_clase_Notebook(self):
    notebook = Notebook(1)
    self.assertTrue("utilizar" in dir(notebook) and callable(notebook.utilizar))
    