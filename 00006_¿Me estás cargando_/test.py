  
  def test_el_método_esta_descargado_está_definido_en_la_clase_Dispositivo(self):
    dispositivo = Dispositivo(1)
    self.assertTrue("esta_descargado" in dir(dispositivo) and callable(dispositivo.esta_descargado))
    
  def test_una_notebook_está_descargada_cuando_tiene_menos_de_20_de_batería(self):
    notebook = Notebook(100)
    notebook.utilizar(81)
    self.assertTrue(notebook.esta_descargado())
    
  def test_una_notebook_está_descargada_cuando_tiene_20_de_batería(self):
    notebook = Notebook(100)
    notebook.utilizar(80)
    self.assertTrue(notebook.esta_descargado())

  def test_una_notebook_no_está_descargada_cuando_tiene_más_de_20_de_batería(self):
    notebook = Notebook(100)
    notebook.utilizar(79)
    self.assertFalse(notebook.esta_descargado())
  
  def test_un_celular_está_descargado_cuando_tiene_menos_de_20_de_batería(self):
    celular = Celular(100)
    celular.utilizar(162)
    self.assertTrue(celular.esta_descargado())

  def test_un_celular_está_descargado_cuando_tiene_20_de_batería(self):
    celular = Celular(100)
    celular.utilizar(160)
    self.assertTrue(celular.esta_descargado())
    
  def test_un_celular_no_está_descargado_cuando_tiene_más_de_20_de_batería(self):
    celular = Celular(100)
    celular.utilizar(158)
    self.assertFalse(celular.esta_descargado())
    
  def test_la_clase_Dispositivo_define_el_método_esta_descargado(self):
    dispositivo = Dispositivo(100)
    self.assertTrue("esta_descargado" in dir(dispositivo) and callable(dispositivo.esta_descargado))
