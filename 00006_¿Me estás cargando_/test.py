  
  def test_El_método_esta_descargado_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("sin_carga" in dir(dispositivo) and callable(dispositivo.sin_carga))
    
  def test_Una_notebook_está_sin_carga_cuando_tiene_menos_de_20_de_batería(self):
    notebook = Notebook(19)
    self.assertTrue(notebook.sin_carga())
    
  def test_Una_notebook_está_sin_carga_cuando_tiene_20_de_batería(self):
    notebook = Notebook(20)
    self.assertTrue(notebook.sin_carga())

  def test_Una_notebook_no_está_sin_carga_cuando_tiene_más_de_20_de_batería(self):
    notebook = Notebook(21)
    self.assertFalse(notebook.sin_carga())
  
  def test_Una_tablet_está_descargada_cuando_tiene_menos_de_20_de_batería(self):
    tablet = Tablet(19)
    self.assertTrue(tablet.sin_carga())

  def test_Una_tablet_está_descargada_cuando_tiene_20_de_batería(self):
    tablet = Tablet(20)
    self.assertTrue(tablet.sin_carga())
    
  def test_Una_tablet_no_está_sin_carga_cuando_tiene_más_de_20_de_batería(self):
    tablet = Tablet(21)
    self.assertFalse(tablet.sin_carga())