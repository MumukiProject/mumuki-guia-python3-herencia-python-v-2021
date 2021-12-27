¿Te acordas de los dispositivos electronicos? ¡Volvieron en forma de herencia! :grimacing:.

En esta oportunidad vamos a modelar `Tablet`s , de las cuales sabemos:

* tienen una bateria, que se puede indicar inicialmente;
* entienden el mensaje `tiene_bateria` que indica si su batería es mayor a 20;
* cuando utilizamos una `Tablet`, su batería disminuye en la mitad de los minutos que lo hagamos. Por ejemplo: si usamos la tablet 30 minutos, su batería bajará en 15;
* las `Tablet`s se pueden `cargar_a_tope` para dejar la batería en 100. 
* Y entienden el mensaje `tiene_bateria_maxima` que indica si la misma está exactamente al 100%.

> Veamos si se entiende: Definí en la clase `Tablet` que sepa entender los mensajes `__init__`, `utilizar`, `tiene_bateria`,  `tiene_bateria_maxima` y `cargar_a_tope`.