#Obtener la edad de una persona en meses, si se ingresa su edad en años y meses
#Ejemplo:Ingresando 3 años 4 meses debe mostrar 40 meses

print("Bienvedido al Programa".center(50,"-"))

años = 0
meses = 0

años = int(input("Ingrese años: "))
meses = int(input("Ingrese meses: "))

print("Total: ",(años*12)+ meses," meses")
