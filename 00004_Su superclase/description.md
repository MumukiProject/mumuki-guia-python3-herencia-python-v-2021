Una forma de organizar las clases cuando programamos en objetos es definir una **jerarquía**. En nuestro caso podemos pensar que `Celular` y `Notebook` se pueden englobar en algo más grande y que las incluye, la idea de `Dispositivo`. :iphone::computer:

Muchas veces esa jerarquía se puede visualizar en el mundo real: por ejemplo, `Perro` y `Gato` entran en la categoría `Mamifero`, mientras que `Cóndor` y `Halcón` se pueden clasificar como `Ave`. Cuando programemos, la jerarquía que utilicemos dependerá de nuestro modelo y de las abstracciones que utilicemos.

```python
class Ave:
  def __init__(self, energia):
    self.energia = energia
  def volar(self):
    self.energia -= 20

class Condor(Ave):
  def dormir(self,minutos):
   self.energia += minutos * 3

class Halcon(Ave):
  def dormir(self,minutos):
   self.energia += minutos

```

Cuando escribimos entre paréntesis el nombre de la súper clase significa "hereda de": por ejemplo, `Condor` hereda de `Ave`, que está _más arriba_ en la jerarquía. Otra manera de decirlo es que cada `Condor` es una `Ave`.

La herencia nos permite que las *subclases*  (`Condor` y `Halcon`) posean los mismos métodos y atributos que la *superclase* `Ave`. Es decir, las instancias de `Condor` y de `Halcon` van a saber `volar` de la misma forma, pero cuando les enviemos el mensaje `dormir` cada una hará algo diferente.

¡Uf! ¡Eso fue un montón! :fearful: A ver si quedó claro. 

> Definí la clase `Dispositivo` y modificá las clases que definiste anteriormente para evitar que haya métodos repetidos entre `Celular` y `Notebook`. Es importante que en el editor definas arriba la superclase y abajo sus subclases.