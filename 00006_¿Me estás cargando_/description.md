Ya aprendimos en este recorrido cómo funciona el method lookup, el proceso por el cual cuando le enviamos un mensaje a un objeto, este busca en su clase la definición del método asociado. :nerd:

Al tratar con herencia, cambian un poquito las cosas. Si bien el objeto va a seguir preguntándole a su clase qué debe hacer al recibir el mensaje, en caso de no encontrar un método asociado no va a lanzar una excepción sino que se va a fijar en su superclase. En caso de no encontrar la definición seguirá "subiendo" en la jerarquía de clases y solo fallará nuestro código si el método no fue encontrado en ninguna de ellas. :arrow_up:

Probemos si se entendió modelando una gran molestia de los dispositivos electrónicos: la falta de carga. En otras palabras, cuando el dispositivo no `tiene_bateria`. :battery:

> Definí el método `sin_carga` de forma tal que al recibir ese mensaje tanto `Tablet`s como `Notebook`s hagan lo mismo.