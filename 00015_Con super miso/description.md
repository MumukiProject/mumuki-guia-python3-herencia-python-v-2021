Si prestamos atención a los constructores de `Colectivo` y `MedioDeTransporte` podremos notar que hay cierta lógica repetida dado que ambos métodos `__init__` se encargan de establecer un `combustible` inicial. 

Por suerte, en el ejercicio anterior conocimos a `super`, pero ¿cómo puede ayudarnos a resolver esta repetición? :thinking:

Volvamos a las aves un momento e imaginemos que los halcones siempre tienen una energía inicial igual a 80. Para evitar repetir lógica entre las clases `Ave` y `Halcon` podríamos hacer lo siguiente:

```python
class Ave:

  def __init__(self, energia):
    self.energia = energia

  def volar(self):
    self.energia -= 20

class Halcon(Ave):
  # no redefinimos el constructor, 
  # por lo que para instanciar un halcón
  # debemos pasarle una cantidad de energia

  def dormir(self,minutos):
    self.energia += minutos

class Condor(Ave):
  # redefinimos el constructor de condor, 
  # de forma que no haya que pasarle una cantidad
  # de energia, sino que siempre inicie con 80

  def __init__(self):
    super().__init__(80)

  def dormir(self,minutos):
    self.energia += minutos * 3
```

Es más, si tuvieramos una `Golondrina` que sabe su ubicación actual podríamos hacer lo siguiente: 

```python
class Golondrina(Ave):
  # en golondrina también redefinimos el constructor, 
  # pero para agregar parámetros, por lo que para instanciarla
  # deberemos pasarle energía y una ubicación
  
  def __init__(self, energia, ubicacion):
    super().__init__(energia)
    self.ubicacion = ubicacion
    
    
  # ...resto del código...
```


:warning: Como se ve en estos ejemplos, a diferencia de lo que que ocurre con el resto de los métodos, al redefinir `__init__` no tenemos la obligación de respetar la cantidad de parámetros de la versión original: 

  * podemos mantenerla;
  * podemos remover parámetros (como en `Condor`);
  * podemos agregar parámetros (como en `Golondrina`);
  * ¡o cualquier otra combinación!

Eso sí, siempre tenemos que tener el cuidado de llamar a `super().__init__(...)` con **todos** los argumentos que necesite. 

> Modificá el constructor de la clase `Colectivo` para que usando `super` evite repetir lógica con la clase `MedioDeTransporte`. 