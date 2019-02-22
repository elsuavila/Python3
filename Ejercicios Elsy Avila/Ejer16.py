#Suponga que un individuo desea invertir su capital en un banco y desea saber
#cuanto dinero ganara despues de un año si el banco paga a razon de 2,5% mensual

print("Bienvedido al Programa".center(50,"-"))

PORCENTAJE = 0.025
capital = 0
capital = int(input("ingrese el capital a invertir:"))
mult = capital *PORCENTAJE
total = mult * 12
print ("El dinero a ganar en un año es de:{}".format(total))

