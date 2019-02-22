#un alumno desea saber cual sera su clasificacion final en la materia de
#algoritmos dicha calificacion se compone de tres examenes parciales


print("Ingrese sus nota ".center(50,"-"))

Calificacion = 0


Parcial1 = int(input("Ingrese su nota:."))
Parcial2 = int(input("Ingrese su nota:."))
Parcial3 = int(input("Ingrese su nota:."))

Calificacion = float((Parcial1 + Parcial2 +Parcial3 )/3)
print ("La Calificacion es :. {}".format(Calificacion))
            
