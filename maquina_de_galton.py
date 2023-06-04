import random
import matplotlib.pyplot as plt

def simular_maquina_galton(niveles, canicas):
    contadores = [0] * (niveles + 1)

    for _ in range(canicas):
        contador = 0
        for _ in range(niveles):
            lado = random.choice([0, 1])
            contador += lado
        contadores[contador] += 1

    return contadores

def graficar_histograma(contadores):
    niveles = len(contadores)
    x = range(niveles)
    y = contadores

    plt.bar(x, y)
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de la Máquina de Galton')

    plt.show()

resultados = simular_maquina_galton(12, 3000)
graficar_histograma(resultados)
