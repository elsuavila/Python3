#Calcular el nuevo salario de un empleado si se le descuenta el 20& de su
#Salario actual

print("Bienvedido al Programa".center(50,"-"))

salario = 0
Descuento = 0

salario = float(input("Ingrese salario actual:."))
Descuento = salario * 0.20

print("El salario total es de :. {}".format(salario-Descuento))
