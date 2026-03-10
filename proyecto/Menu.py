''' 
Creado en Marzo del 2026
@autor: Ricardo-NR 
'''

from Auto import *

class Menu:

	def __init__(self, valor):
		self.mensajeDeBienvenida = valor
		
	def darBienvenida(self):
		print(self.mensajeDeBienvenida)

	def despliegaMenu(self):
		print("Las opciones son:")
		print("1. Mostrar los autos guardados")
		print("2. Autos disponibles")
		opcion = input("Teclea la opcion:")
		
