
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