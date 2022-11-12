# Python 

> P1.¿Que es una clase abstracta?

- [x]  Una clase abstracta existe solo para que otras clases "concretas" puedan heredar de la clase abstracta.

> P2.¿Qué sucede cuando usa la función incorporada "any()" en una lista?

- [x] La función “any()” devuelve True si algún elemento de la lista se evalúa como True. De lo
contrario, devuelve False.

> P3.¿A qué estructura de datos degenera un árbol binario si no está equilibrado correctamente?

- [x] Colas

> P4.¿Qué es un método estático?
- [x]  Sirven principalmente como métodos de utilidad o métodos auxiliares, ya que no pueden acceder ni modificar el estado de una clase.

>P5.¿Qué son los atributos?
- [x]  Los argumentos de función se denominan "atributos" en el contexto de los métodos de 
clase y los métodos de instancia.

> P6.¿Qué método de lista usaría para eliminar elementos de una lista?
- [x] método “.pop()”

> P7.¿Cuál es el tiempo de ejecución para acceder a un valor en un diccionario usando su clave?
- [x]  “O(1)”, también llamado tiempo constante

> P8.¿Cuál es la forma correcta de escribir un doctest?
- [x] def sum(a, b): <br>
“““<br>
sum(4, 3)<br>
7<br>
sum(-4, 5)<br>
1<br>
”””<br>
return a + b

>P9.¿Cómo funciona "defaultdict"?
- [x]  Si intenta acceder a una clave en un diccionario que no existe, "defaultdict" creará una nueva clave, en lugar de arrojar un "KeyError".

>P10. ¿Cuál es el propósito de la palabra clave "self" al definir o llamar a métodos de instancia?
- [x]  self se refiere a la instancia cuyo método fue llamado.

>P11. ¿Qué afirmación NO describe el concepto de encapsulación de la programación orientada a objetos?
- [x]  Una clase principal está encapsulada y ningún dato de la clase principal pasa a la clase secundaria

>P12. ¿Qué tipo de datos incorporado en Python se usa comúnmente para representar una cola?
- [x] Lista

>P13. ¿Qué hace la función integrada map()?
- [x]  Aplica una función a cada elemento en un iterable y devuelve el valor de esa función.

> P14. Si no devuelve explícitamente un valor de una función, ¿qué sucede?
- [x]  Si la palabra clave return está ausente, la función devolverá None.

>P15. De acuerdo con las pautas de estilo de codificación de PEP 8, ¿cómo se deben nombrar los valores constantes en Python?
- [x]  En mayúsculas con guiones bajos que separan las palabras, ejem. MAX_VALUE = 255