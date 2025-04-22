print("De dos numeros te dire cual es el mayor o si son iguales")
numero1 = float(input("Dame el primer numero "))
numero2 = float(input("Ahora el segundo numero "))
if numero1 > numero2:
    print(f"El numero {numero1:.2f} es mayor!")
elif numero2 > numero1:
    print(f"El numero {numero2:.2f} es mayor!")
else:
    print("Ambos son iguales!")