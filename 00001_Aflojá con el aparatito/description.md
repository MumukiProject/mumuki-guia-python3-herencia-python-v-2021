¿Te acordás de los dispositivos electrónicos? ¡Volvieron en forma de `Tablet`s! :grimacing:

Para ello vamos a modelarlas teniendo en cuenta que:

* tienen una bateria, que se puede indicar inicialmente;
* entienden el mensaje `tiene_bateria` que indica si su batería es mayor a 20;
* cuando utilizamos una `Tablet`, su batería disminuye en la mitad de los minutos que lo hagamos. Por ejemplo: si usamos la tablet 30 minutos, su batería bajará en 15;
* se pueden `cargar_a_tope` para dejar la batería en 100. 
* entienden el mensaje `tiene_bateria_maxima` que indica si la misma está exactamente al 100%.

> Veamos si se entiende: Definí la clase `Tablet` con su constructor, y sus métodos `utilizar`, `tiene_bateria`,  `tiene_bateria_maxima` y `cargar_a_tope`.