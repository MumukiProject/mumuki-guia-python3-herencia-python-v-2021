
  def test_Una_Tablet_gasta_30_de_bateria_si_la_uso_una_hora(self):
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
    tablet = Tablet(10)
    tablet.cargar_a_tope()
    self.assertEqual(tablet.bateria,100)
    
  def test_Una_tablet_tiene_bateria_maxima_si_tiene_100_de_bateria(self):
    tablet = Tablet(100)
    self.assertTrue(tablet.tiene_bateria_maxima)
    
  def test_Una_tablet_no_tiene_bateria_maxima_si_tiene_menos_de_100_de_bateria(self):
    tablet = Tablet(99)
    self.assertFalse(tablet.tiene_bateria_maxima)
    
  def test_una_notebook_tiene_bateria_si_tiene_más_de_20_de_bateria(self):
    tablet = Tablet(21)
    self.assertTrue(tablet.tiene_bateria)  
    
  def test_una_notebook_no_tiene_bateria_si_tiene_20_de_bateria(self):
    tablet = Tablet(20)
    self.assertFalse(tablet.tiene_bateria) 
    
  def test_una_notebook_no_tiene_bateria_si_tiene_menos_de_20_de_bateria(self):
    tablet = Tablet(19)
    self.assertFalse(tablet.tiene_bateria)