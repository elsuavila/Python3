##Elsy
## Calcular la edad actual de una persona,
# previamente ingrensando
# el año ctual y el año de macimiento

print("Bienvenido al programa".center(50,"*"))

FEC_ACT = 2019
fec_nac = int(input("ingresa tu año de nacimiento"))

edad = FEC_ACT - fec_nac


if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

    
print("tu edad es {}".format(edad)) 
