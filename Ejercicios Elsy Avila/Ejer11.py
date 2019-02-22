#Escriba un programa donde se ingrese el tiempo necesario para un cierto proceso en horas
#minutos y seundos;se calcule el costo total del proceso sabiedno que el costo poe segundo es de Bs0,25


print("Bienvedido al Programa".center(50,"-"))

Horas = 0
Minutos = 0
Segundos = 0
Total = 0

Horas = int(input("Ingrese horas:."))
Minutos = int(input("Ingrese minutos:."))
Segundos = int(input("Ingrese segundos"))

Total = (((Horas * 3600) + (minutos * 60 ) + Segundos) * 0.25)
         
print("Costo total del proceso Bs.",Total)
