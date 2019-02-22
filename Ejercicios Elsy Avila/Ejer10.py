#Un constructor sabe que necesita o,5 metros cubicos de arena por metro cuadrado
#De revoque a reaalizar hacer un progroma donde ingrese las medidas de una pared
#(largo y alto) expresada en metros y btenga la cantidad de arena necesaria
#para revolcarla

print("Bienvedido al Programa".center(50,"-"))

Arena_Metro_Cubico = 0.5
Arena = 0
Base = 0
Altura = 0
Arena_Necesaria = 0

Base = float(input("Ingrese base de la pared:."))
Altura = float(input("Ingrese altura de la pared:."))
Area = Base * Altura
Arena_Necesaria = Arena_Metro_Cubico

print("Se necesitan", Area_Necesaria,"Metro CUbicos de arena")
