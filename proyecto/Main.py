''' 
Creado en Marzo del 2026
@autor: Ricardo-NR
'''

from Auto import *
from Menu import *


class Main:
	pass

menu = Menu("Bienvenidos al Sistema de Autos")
menu.darBienvenida()
menu.despliegaMenu()

auto1 = Auto("Toyota", "Corolla", 2020)
auto2 = Auto("Mercedes-Benz", "Clase G", 2025)

print(auto1.marca)
print(auto1.modelo)
print(auto1.año)

print(auto2.marca)
print(auto2.modelo)
print(auto2.año)

print("\n\n*** 2. Imprimimos los autos guardados")
auto1.imprimirDetalles()
auto2.imprimirDetalles()