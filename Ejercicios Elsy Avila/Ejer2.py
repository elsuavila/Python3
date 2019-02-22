#Calcula el preio de unboleto de viaje, tomando en cuenta el numero de kilometros
#que se van a ecorrer, siend el precio BS/.10,50 por km.


print("bienvenidos al programa".center(50,"-"))

Precio_km = 10.50
kms = 0
total = 0

kms = float(input("Ingrese kilometros a recorrer:."))
total = Precio_km * kms

print("Precio del boleto: Bs.",total)
