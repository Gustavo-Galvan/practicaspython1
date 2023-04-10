personas = 0

while True: 
    nombre = input("Ingrese su nombre: ")
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = peso / (altura ** 2)
    
    es_mayor_edad = edad >= 18
    
    print("----- RESULTADOS -----")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años ({'mayor' if es_mayor_edad else 'menor'} de edad)")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")
    
    if imc < 18.5:
        print("Estado de peso: bajo peso")
    elif imc < 25:
        print("Estado de peso: peso normal")
    elif imc < 30:
        print("Estado de peso: sobrepeso")
    else:
        print("Estado de peso: obesidad")
    
    personas += 1
    
    continuar = input("¿Desea realizar otra medición? (s/n) ")
    if continuar.lower() != "s":
        break
    
print(f"El código ha sido utilizado por {personas} persona(s).")