while True:
    palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
    if palabra == "salir":
        break

    longitud = len(palabra)

    if longitud >= 4 and longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")

if len(palabra1) < 2:
    palabra1 = "X" + palabra1
if len(palabra2) < 2:
    palabra2 = "X" + palabra2
if len(palabra3) < 2:
    palabra3 = "X" + palabra3

contraseña = palabra1[0] + palabra2[0] + palabra3[0] + palabra1[1] + palabra2[1] + palabra3[1]
print("La contraseña es:", contraseña)

while True:
    contraseña_usuario = input("Introduce la contraseña: ")

    if len(contraseña_usuario) < len(contraseña):
        print("Faltan", len(contraseña) - len(contraseña_usuario), "caracteres")
    elif len(contraseña_usuario) > len(contraseña):
        print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
    elif contraseña_usuario == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Vuelve a intentarlo.")
        