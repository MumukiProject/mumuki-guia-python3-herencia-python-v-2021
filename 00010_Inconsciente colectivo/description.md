No hay 2 sin 3, tampoco hay 20 sin 21, o 30...

La verdad es que la cantidad de gente que puede entrar en un `Colectivo` es variable, y para simplificar las cosas vamos a decir que en un colectivo siempre entran personas. :bus:

Pero... ¿entonces no es un `MedioDeTransporte`? :thinking:

Sí, en realidad es un `MedioDeTransporte`, solo que responde distinto a `entran_personas`. Lo que podemos hacer es **redefinir el método**: si `Colectivo` define el método `entran_personas` va a evaluar ese código en lugar del de su superclase.

Ahora que sabemos que se pueden redefinir métodos, aprovechemos y cambiemos un poco más nuestra solución:

* Los colectivos siempre se inicializan con 100 de `combustible` y con 0 `pasajeros`;
* ya no necesitamos el método `maximo_personas` porque siempre entran personas.

> Redefiní los métodos `__init__` y `entran_personas` en la clase `Colectivo`, también eliminá el método `maximo_personas` de la misma clase.