#Escriba un algortiml que dado el numero de horas trabajadas por un empleado y
#El sueldo por hora, calcule el sueldo total de ese empleado.Tenga en cuento que las horas extras
#se pagan al doble.
print("Bienvedido al Programa".center(50,"-"))
Sueldo = 0
Horas_Trab = 0
Horas_Extras = 0
Total_Trab = 0
Total_Extras = 0
Total = 0

Suledo = float(input("Ingrese sueldo por hora:."))
Horas_Trab = float(input("Ingrese cantidas de horas trabajadas:."))
Horas_Extras = float(input("Ingrese cantidad de de horas extras:."))
Total_Trab = Sueldo * Horas_Trab
Total_Extras = Sueldo * Horas_Extras *2
Total = Total_Tab + Total_Extras

print ("Sueldo por horas:." ,Total_Trab)
print ("Sueldo por horas extras:." ,Total_Extras)
print ("Sueldo total:.", Total)
