Desconectémonos un poco y salgamos de paseo. ¿En qué vamos? :thinking:

Por ahora nuestras opciones son limitadas. Podemos elegir ir en `Auto` o en `Moto`. De ambos medios sabemos que: 

* ambos vehículos comienzan con una cantidad que podemos establecer de `combustible`;
* los autos pueden llevar 5 personas como máximo y al `recorrer` una distancia consumen medio litro de `combustible` por cada kilómetro recorrido;
* las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
* ambos pueden `cargar_combustible` en la cantidad que digamos y al hacerlo suben su cantidad de `combustible`;
* ambos vehículos saben responder si `entran_personas`. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

¡Vamos a modelar todo esto! :red_car: :motorcycle:

> Definí las clases `Moto`, `Auto` y `MedioDeTransporte` y hace que las dos primeras hereden de la tercera. También definí los métodos `__init__`, `recorrer`, `cargar_combustible`, `entran_personas` y `maximo_personas` donde correspondan.
