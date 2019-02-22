#Calcula el nuevo salario de un obrero si obtuvo un incremento del 25%
#sobre su salario anterior

print("Bienvenido al program ".center(50,"-"))

salario = 0
Incremento = 0
Total = 0

salario = int(input("Ingrese salario :."))
Incremento = salario * 0.25
Total = salario + Incremento
print("El incremento es:.",Incremento)

print("\nsalario actual:.",Total)
