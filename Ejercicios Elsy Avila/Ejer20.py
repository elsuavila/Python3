#Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres
#hay en un grupo de estudiantes

print("Ingrese sus nota ".center(50,"-"))

PORCENTAJE = 0.15
hombres = 0
mujeres = 0
hombres = int(input("ingrese cantidad de hombres"))
mujeres = int(input("ingrese cantidad de mujeres"))
porcentaje_h = hombres * PORCENTAJE
porcentaje_m = mujeres * PORCENTAJE
print("el porcentaje de hombres es de:{}".format(porcentaje_h))
print("el porcentaje de muejeres es de:{}".format(porcentaje_m))

