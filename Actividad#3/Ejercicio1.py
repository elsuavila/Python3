#Elsy
#Ejercicio1
#Que seleccione una opcion
#opcion 1. solicitar dos numeros y elevar el primer numero al segundo numero
#opcion 2.solicitar tres numeros y elevar el primero al segundo
#y el resultado elevar al tercero
print("Bienvenido selecicione una opcion".center(50,"-"))
print("1.opcion 2.opcion".center(81,"*"))
opcion = input (":.")

if opcion == "1":
    numero1 = input("ingrese primer numero")
    numero2 = input("ingrese el segundo numero")
    elevacion = int(numero1) ** int(numero2)
    print("la levacion es:. {}".format(elevacion))
elif opcion == "2":
    numero1 = input("ingrese el primer numero")
    numero2 = input("ingrese segundo numero")
    numero3 = input("ingrse el tercer numero")
    elevacion = int(numero2) ** int(numero1) ** int(numero3)
    print("la levacion es:. {}".format(elevacion))
    
  
