
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
    
  def test_Una_notebook_vuelve_a_tener_100_de_bateria_si_la_cargo_a_tope(self):
    notebook = Notebook(10)
    notebook.cargar_a_tope()
    self.assertEqual(notebook.bateria,100)

  def test_una_notebook_tiene_bateria_maxima_si_la_tiene_100_de_bateria(self):
    notebook = Notebook(100)
    self.assertTrue(notebook.tiene_bateria_maxima)
    
  def test_una_notebook_tiene_bateria_maxima_si_la_tiene_menos_de_100_de_bateria(self):
    notebook = Notebook(99)
    self.assertFalse(notebook.tiene_bateria_maxima())
  
  def test_una_notebook_tiene_bateria_si_tiene_más_de_20_de_bateria(self):
    notebook = Notebook(21)
    self.assertTrue(notebook.tiene_bateria())  
    
  def test_una_notebook_no_tiene_bateria_si_tiene_20_de_bateria(self):
    notebook = Notebook(20)
    self.assertFalse(notebook.tiene_bateria())  
    
  def test_una_notebook_no_tiene_bateria_si_tiene_menos_de_20_de_bateria(self):
    notebook = Notebook(19)
    self.assertFalse(notebook.tiene_bateria())  