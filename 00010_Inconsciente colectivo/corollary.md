¡Genial! :tada:

Esto de la herencia está buenísimo. Porque nos permite heredar el comportamiento de una superclase pero redefinir aquellas cosas que nuestras subclases hacen distinto:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-herencia-python-v-2021/master/assets/clases_4.10.svg" alt="Diagrama de clases" width="800px" height="auto">

:warning: Eso sí, hay que tener cuidado con la cantidad de parámetros: como regla general, al redefinir, los nuevos métodos deben tomar **la misma cantidad de parámetros que los métodos originales**.  

Además, si tenemos que redefinir todo probablemente no necesitemos heredar en primer lugar. ¿Y qué pasa cuando en una subclase no hago lo mismo que en la superclase pero tampoco es taaaan diferente? :thought_balloon:

¡Vamos a averiguarlo!