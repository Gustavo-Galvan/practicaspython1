# Pidiendo los datos al usuario
nombre = input("Por favor, ingresa tu nombre por favor: ")
apellido_paterno = input("Ingresa tu apellido paterno por favor: ")
apellido_materno = input("Ingresa tu apellido materno por favor: ")
peso = float(input("Ingresa tu peso en kilogramos por favor: "))
estatura = float(input("Ingresa tu estatura en metros por favor: "))

# Calculando el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Imprimiendo el resultado del IMC y si hay sobrepeso o no
print(f"{nombre} {apellido_paterno} {apellido_materno}, tu índice de masa corporal (IMC) es de: {imc:.2f}")

if imc < 18.5:
    print("Tienes un peso inferior al normal.")
elif 18.5 <= imc < 25:
    print("Tienes un peso normal.")
elif 25 <= imc < 30:
    print("Tienes sobrepeso.")
elif 30 <= imc < 40: 
    print("Tienes obesidad.")