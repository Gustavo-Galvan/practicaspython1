# practicaspython1
personas = 0  # Contador de personas que han utilizado el código

while True:  # Ciclo infinito para permitir múltiples mediciones
    nombre = input("Ingrese su nombre: ")
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    # Cálculo del índice de masa muscular (IMC)
    imc = peso / (altura ** 2)
    
    # Comprobación de si el usuario es mayor de edad
    es_mayor_edad = edad >= 18
    
    # Impresión de los resultados
    print("----- RESULTADOS -----")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años ({'mayor' if es_mayor_edad else 'menor'} de edad)")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")
    
    # Comprobación del estado de peso
    if imc < 18.5:
        print("Estado de peso: bajo peso")
    elif imc < 25:
        print("Estado de peso: peso normal")
    elif imc < 30:
        print("Estado de peso: sobrepeso")
    else:
        print("Estado de peso: obesidad")
    
    personas += 1  # Incremento del contador de personas
    
    # Preguntar si desea realizar otra medición
    continuar = input("¿Desea realizar otra medición? (s/n) ")
    if continuar.lower() != "s":
        break  # Salir del ciclo si la respuesta es diferente a "s"
    
print(f"El código ha sido utilizado por {personas} persona(s).")
