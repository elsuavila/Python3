# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8%
#Sobre su salario actual y un descuento de 2,5% por servicios

print("Bienvedido al Programa".center(50,"-"))

Salario = 0
Incremento = 0
Descuento = 0
Total = 0

Salario = float(input("Ingrese su salario actual:."))
Incremento = Salario * 0.08
Descuento = Salario * 0.025
Total = Salario + Incremento - Descuento
print("El incremento es:.",Incremento)
print("El Descuento es:.",Descuento)

print("\nSalario actual:.",Total)
