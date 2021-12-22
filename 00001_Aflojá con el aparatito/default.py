class Celular:
  
  def __init__(self, bateria, saldo, sistema_operativo):
    self.bateria = bateria
    self.saldo = saldo
    self.sistema_operativo = sistema_operativo

  def tiene_bateria(self):
    return self.bateria > 20

  def tiene_bateria_maxima(self):
    return self.bateria == 100

  def necesita_saldo(self):
    return self.saldo == 0
    
  def cargar_saldo(self, saldo):
    return self.saldo += saldo
