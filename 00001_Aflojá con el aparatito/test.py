
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