class Zombi:
  def __init__(self,salud_inicial):
    self.salud = salud_inicial
  
  def salud(self):
    return self.salud
  
  def gritar(self):
    return "¡agrrrg!"
  
  def sabe_correr(self):
    return False
  
  def sin_vida(self):
    return self.salud == 0
  
  def recibir_danio(self,puntos):
    self.salud = max(self.salud - puntos * 2, 0)


class SuperZombi:
  def __init__(self,salud_inicial):
    self.salud = salud_inicial

  def salud(self):
    return self.salud

  def gritar(self):
    return "¡agrrrg!"

  def sabe_correr(self):
    return True

  def sin_vida(self):
    return self.salud == 0

  def recibir_danio(self,puntos):
    self.salud = max(self.salud - puntos * 3, 0)
  
  def regenerarse(self):
    self.salud = 100
