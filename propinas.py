total = float(input("Cuanto fue el total de la cuenta? "))

porcentaje = int(input("Que porcentaje de propina deseas dejar? (10, 15 o 20%) "))
if porcentaje in [10, 15, 20]:
    propina = total * (porcentaje / 100)
    print(f"La propina es de ${propina:.2f}")
else:
    print("Porcentaje no valido, debe ser 10, 15 o 20")