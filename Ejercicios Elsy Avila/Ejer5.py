#Calcular el descuento y el monto a paagar por un medicamento cualquiera en una
#Farmacia si todos los medicamentos tienen un descuento del 35%

print("Bienvedido al Programa".center(50,"-"))


Precio = 0
Descuento = 0

Precio = float(input("ingrese el precio del medicamneto:."))
Descuento = Precio * 0.35

print("El precio del medicamento es {}".format(Precio-Descuento))
