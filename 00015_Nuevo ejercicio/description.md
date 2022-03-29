Si prestamos atención a los constructores de `Colectivo` y `MedioDeTransporte` podremos notar que hay cierta lógica repetida. Ambos métodos `__init__` se encargan de establecer un `combustible` inicial. 

Por suerte, en el ejercicio anterior conocimos a `super`, pero ¿cómo puede ayudarnos a resolver esta repetición? :thinking:

Volvamos a las aves un momento e imaginemos que los halcones siempre tienen una energía inicial igual a 80. Para evitar repetir lógica entre constructores podríamos hacer lo siguiente:

```python
class Ave:

  def __init__(self, energia):
    self.energia = energia

  def volar(self):
    self.energia -= 20

class Halcon(Ave):

  def __init__(self):
    super().__init__(80)

  def dormir(self,minutos):
   self.energia += minutos

class Condor(Ave):

  def dormir(self,minutos):
   self.energia += minutos * 3
```

> Modificá el constructor de la clase `Colectivo` para que usando `super` evite repetir lógica con la clase `MedioDeTransporte`. 