''' 
Creado en Febrero del 2026
@autor: Ricardo-NR

'''
from Cuenta import *
from Menu import *


class Main:
	pass

menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()
menu.despliegaMenu()

#la cantidad de argumentos que se le pasa al constructor, cambia
cuenta1 = Cuenta( 300, "debito" )

#si fueran muchos atributos, acá aparecerían muchisimas 
#lineas
print (cuenta1.cantidad)
print (cuenta1.tipo)

print ("\n\n*** 2. Imprimimos atributos con el método")
cuenta1.imprimirDetalles()

cuenta1.depositar(800)
cuenta1.imprimirDetalles()