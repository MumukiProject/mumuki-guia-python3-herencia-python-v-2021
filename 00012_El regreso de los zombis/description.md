¿Creíste que habíamos terminado con los zombis? ¡Nada más alejado de la realidad! :fearful: 

Cuando surgieron los `SuperZombi`, notamos que parte de su comportamiento era compartido con un `Zombi` común, en ambos casos podemos especificar su `hambre` inicial y responden al mensaje `sabe_correr` de la misma forma. Pero hasta allí llegan las similitudes: `recibir_danio` y `es_un_peligro` son distintos, y además, un `SuperZombi` puede `regenerarse`, a diferencia de un `Zombi`.

¡Esto nos da una nueva posibilidad! Podemos hacer que `SuperZombi` herede de `Zombi` para:

* Evitar **repetir la lógica** de aquellos métodos que son iguales, ya que se pueden definir únicamente en la superclase `Zombi`;
* **redefinir** en `SuperZombi` aquellos métodos cuya definición sea distinta a la de `Zombi`;
* definir **únicamente** en `SuperZombi` el comportamiento que es exclusivo a esa clase.

> ¿Te animás? ¡Marcá las respuestas correctas!

