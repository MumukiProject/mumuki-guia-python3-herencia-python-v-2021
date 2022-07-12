Bien sabemos que los colectivos también necesitan cargar combustible como cualquier `MedioDeTransporte`, pero ¡qué molesto para los pasajeros! Es por esto que cuando un `Colectivo` carga combustible, además de incrementarlo pierde a todos sus `pasajeros`. :pensive:

Pero si redefinimos `cargar_combustible` en `Colectivo`, ¿cómo hacemos para no repetir lógica con nuestra superclase `MedioDeTransporte`? ¡Con `super`! :muscle:

Al utilizar `super` en el método de una subclase, **se evalúa el método con el mismo nombre de su superclase y además lo que se está redefiniendo**. Por ejemplo:


```python
class Saludo:
  def saludar(self):
    return "Buen día"

class SaludoDocente(Saludo):
  def saludar(self):
    return super().saludar() + " estudiantes"
```

De esta forma, al enviar el mensaje `saludar` a `SaludoDocente`, `super` **invoca** el método `saludar` de su superclase, `Saludo`. :wave: 

```python
ム mi_saludo = SaludoDocente()
ム mi_saludo.saludar()
"Buen día estudiantes"
```

Como podemos notar, `super` en cierta forma modifica como se comporta el method lookup.

> ¡Ahora te toca a vos! Redefiní el método `cargar_combustible` en `Colectivo`, de modo que haga lo mismo que cualquier `MedioDeTransporte` y además se quede sin pasajeros. Recordá utilizar `super` para evitar repetir lógica.