#En  un hospital existen 3 areas: urgencias,pediatria y traumologia
#El presupuesto anual del hospital se reparte de la sguiente manera


print("Bienvedido al Programa".center(50,"-"))

Urgencia = 0
Pediatria = 0
Traumatologia = 0
Presupuesto = 0


Presupuesto = float(input("Ingrese presupuesto anual para el hospital:."))
Urgencia = Presupuesto * 0.37
Pediatria = Presupuesto * 0.42
Traumatologia = Presupuesto * 0.21


print("El area de urgencias recibira la cantidad de dinero de:.",Urgencia)
print("El area de pediatria recibira la cantidad de dinero de:.",Pediatria)
print("El area de Traumotologia recibira la cantidad de dinero de:.",Traumatologia)
