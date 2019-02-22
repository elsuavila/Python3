# Calcular el cambio de monedas en dolares y euros al ingresar cie+ierta cantidad en
#Bs(tipo de cambio $ = 2150Bs, Euros 1,45

print("Bienvedido al Programa".center(50,"-"))

Dolares = 2150
Euros = 3117.5
Cantidad = 0
total = 0

Opcion = int(input("\n1.Dolares a Bs\n2.Euros a Bs \n 	Ingrese su opcion :."))

if Opcion == 1:
     Cantidad = float(input("Ingrese cantidad de dolares:."))
     total = Cantidad * Dolares
     print ("Su total es :. {}".format(total))
elif Opcion == 2:
    Cantidad = float(input("Ingrese Cantidad en Euros:."))
    total = Cantidad * Euros
    print ("Su total es :. {}".format(total))
   
else:
    print("Opcion incorrecta")
