#Una tienda ofrce un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera
#pagar finalmente por su compra


print("Bienvedido al Programa".center(50,"-"))

Precio = 0
Descuento = 0

Precio = float(input("ingrese el precio de su compra:."))
Descuento = Precio * 0.15

print("El precio de la compra a pagar es {}".format(Precio-Descuento))

