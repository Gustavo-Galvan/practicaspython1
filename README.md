# practicaspython1
Primero, definimos una variable llamada num_usuarios que se usará para almacenar el número de personas que han utilizado el programa. Inicializamos esta variable en 0.

A continuación, definimos una función llamada calcular_imc que toma dos parámetros: peso y altura. Esta función calcula el índice de masa corporal (IMC) del usuario usando la fórmula peso / (altura ** 2) y devuelve el resultado.

Luego, solicitamos al usuario que ingrese su nombre, apellido paterno, apellido materno, edad, peso y altura. Para hacer esto, utilizamos la función input y guardamos los valores ingresados por el usuario en variables separadas.

Después, llamamos a la función calcular_imc y pasamos los valores de peso y altura ingresados por el usuario como argumentos. Almacenamos el resultado del cálculo en una variable llamada imc.

A continuación, usamos una serie de declaraciones if para determinar si el usuario tiene bajo peso, peso normal, sobrepeso o obesidad, según su IMC. Esto se hace mediante el uso de los valores de referencia estándar del IMC.

Luego, verificamos si el usuario es mayor de edad o no mediante una declaración if. Si el usuario tiene 18 años o más, lo consideramos mayor de edad y almacenamos el valor "mayor" en la variable es_mayor. De lo contrario, lo consideramos menor de edad y almacenamos el valor "menor" en la variable es_mayor.

Después, incrementamos el contador de usuarios en 1.

Finalmente, imprimimos los resultados utilizando la función print. Usamos f-strings para incluir los valores de las variables en el texto del mensaje.

En la última línea del código, imprimimos el número total de usuarios que han utilizado el programa.
