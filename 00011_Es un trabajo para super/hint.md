Para que una clase pueda hacer lo mismo que su superclase y algo más, usaremos `super` de esta manera:

```python
class Perro:
  def cruzarse_con_otro_perro(self):
    self.mover_la_cola()

class PerroCascarrabias(Perro):
  def cruzarse_con_otro_perro(self):
    super().cruzarse_con_otro_perro()
    self.ladrar()
```