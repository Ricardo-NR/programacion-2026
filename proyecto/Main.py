''' 
Creado en Marzo del 2026
@author: Ricardo-NR
'''

from Auto import *
from Menu import *

class Main:
	pass


menu = Menu("Bienvenidos al Sistema de Autos")
menu.darBienvenida()
opcion = menu.despliegaMenu()
menu.procesaOpcion(opcion)
