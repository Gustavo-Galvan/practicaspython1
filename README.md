El código consta de dos funciones principales: simular_maquina_galton() y graficar_histograma().

La función simular_maquina_galton() simula el proceso de una máquina de Galton. Recibe dos parámetros: niveles y canicas. En cada iteración del bucle exterior (que se repite canicas veces), se simula el movimiento de una canica a través de los niveles de obstáculos. Para cada nivel, se selecciona aleatoriamente un lado (0: izquierda, 1: derecha) utilizando random.choice([0, 1]). Dependiendo del lado seleccionado, se incrementa el contador en 1 o se deja igual. Al final de cada iteración, se incrementa el contador correspondiente al nivel donde termina la canica en la lista contadores. Al finalizar todas las iteraciones, se devuelve la lista contadores que contiene el recuento de canicas en cada nivel.

La función graficar_histograma() recibe la lista contadores como parámetro. Utiliza la biblioteca matplotlib.pyplot para crear un histograma de barras. Se define un conjunto de valores x correspondientes a los contenedores y otro conjunto de valores y correspondientes a la cantidad de canicas en cada contenedor. Se utiliza la función plt.bar() para crear el gráfico de barras con los valores x e y. Luego se establecen etiquetas para los ejes x e y con plt.xlabel() y plt.ylabel(), respectivamente. Finalmente, se establece un título para el gráfico con plt.title(). Finalmente, se muestra el gráfico utilizando plt.show().

En la parte final del código, se invoca la función simular_maquina_galton() pasando los valores 12 para niveles y 3000 para canicas, y se guarda el resultado en la variable resultados. Luego, se invoca la función graficar_histograma() pasando resultados como argumento para generar y mostrar el histograma.

Este código simula el proceso de una máquina de Galton con obstáculos y muestra un histograma que representa la cantidad de canicas en cada nivel después de realizar la simulación.
