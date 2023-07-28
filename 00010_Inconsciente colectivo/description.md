No hay 2 sin 3, tampoco hay 20 sin 21, o 30...

La verdad es que la cantidad de gente que puede entrar en un `Colectivo` es variable, y para simplificar las cosas vamos a decir que en un colectivo siempre entran personas. :bus:

Pero... ¿entonces no es un `MedioDeTransporte`? :thinking:

Sí, en realidad es un `MedioDeTransporte`, solo que responde distinto a `entran_personas`. Lo que podemos hacer es **redefinir el método** `entran_personas`: definir nuevamente este método en `Colectivo`, pero dejando también su versión original en `MedioDeTransporte`. Algo así: 


```python
class MedioDeTransporte:
  # ...todo lo anterior queda igual...
  
  def entran_personas(self, cantidad):
    # ...incluso entran_personas queda igual...
    return cantidad <= self.maximo_personas() 


class Colectivo(MedioDeTransporte):
  # ...acá también dejamos todo como estaba...
  
  # ...peeeero redefinimos (es decir, definimos nuevamente)
  # el método entran_personas...
  def entran_personas(self, cantidad):
    # ...y escribimos acá la nueva lógica
    # que sólo aplica a los colectivos
```

Así, gracias al _method lookup_, si tenemos un `Colectivo`...

```python
un_60 = Colectivo(100)
```

...y esta clase define el método `entran_personas`, cuando se envíe dicho mensaje se va a evaluar el nuevo código en lugar del de su superclase.

```python
ムun_60.entran_personas(50) # ahora se evalúa la nueva lógica
True
ムun_60.entran_personas(100)
True
ムun_60.entran_personas(200)
True
```

> Ahora que sabemos que se pueden redefinir métodos, aprovechemos y cambiemos un poco más nuestra solución:
> 
> * Los colectivos siempre se inicializan con 0 `pasajeros`;
> * ya no necesitamos el método `maximo_personas` porque siempre entran personas;
> * y como ya dijimos, debemos hacer que `entran_personas` sea siempre verdadero.
>
> Redefiní los métodos `__init__` y `entran_personas` en la clase `Colectivo`, también eliminá el método `maximo_personas` de la misma clase.