class Celular:
  
  def __init__(self, bateria):
    self.bateria = bateria

  def tiene_bateria(self):
    return self.bateria > 20

  def tiene_bateria_maxima(self):
    return self.bateria == 100
