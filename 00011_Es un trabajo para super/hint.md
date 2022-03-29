Para que una clase pueda hacer lo mismo que su superclase y algo más, usaremos `super` de esta manera:

```python
class Perro:
  def cruzarse_con(self, un_perro):
    self.mover_la_cola()
    self.oler(un_perro)

class PerroCascarrabias(Perro):
  def cruzarse_con(self, un_perro):
    super().cruzarse_con(un_perro)
    self.ladrar()
```