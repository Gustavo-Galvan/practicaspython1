x = float(input("Ingrese la coordenada X del punto: "))
y = float(input("Ingrese la coordenada Y del punto: "))

if x > 0 and y > 0:
    print("El punto está en el cuadrante I")
elif x < 0 and y > 0:
    print("El punto está en el cuadrante II")
elif x < 0 and y < 0:
    print("El punto está en el cuadrante III")
elif x > 0 and y < 0:
    print("El punto está en el cuadrante IV")
elif x == 0 and y == 0:
    print("El punto está en el origen")
else:
    print("El punto está sobre uno de los ejes")
    