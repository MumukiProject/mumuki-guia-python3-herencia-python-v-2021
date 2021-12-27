
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
    tablet = Tablet(100)
    tablet.utilizar(200)
    tablet.cargar_a_tope()
    self.assertEqual(tablet.bateria,100)