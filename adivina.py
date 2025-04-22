numero_secreto = 3
usuario = int (input("Adivina el numero oculto del 1 al 10, cual es?: "))
if usuario == 3:
    print("Ese es el numero secreto!")
elif usuario < 3:
    print("El numero oculto es mayor")
elif usuario > 3:
    print("El numero oculto es menor")