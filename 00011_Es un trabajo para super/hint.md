Para que una clase pueda hacer lo mismo que superclase y algo más, usaremos `super` de esta manera:

```python
class Perro:
  def recibir_duenio(self):
    self.mover_la_cola()

class PerroCascarrabias(Perro):
  def recibir_duenio(self):
    super().recibir_duenio()
    self.ladrar()

```