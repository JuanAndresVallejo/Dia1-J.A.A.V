print("Vamos a calcular tu IMC")
peso = float(input("Cual es tu peso en kilogramos? "))
altura = float(input("Cual es tu altura en metros? "))
imc = (peso / (altura**2))
print(f"Tu IMC es de {imc:.2f}!")
if imc < 18.5:
    print("Estas en bajo peso")
elif 18.5 <= imc < 24.5:
    print("Estas en peso ideal")
elif 25 <= imc < 29.9:
    print("Estas en sobrepeso")
else:
    print("Estas en obesidad")