''' 
Creado en Marzo del 2026
@author: Ricardo-NR
'''

from Auto import *

class Menu:

	def __init__(self, valor):
		self.mensajeDeBienvenida = valor
		self.cargaDatos()

	def cargaDatos(self):
		self.autos = [Auto("Toyota", "Corolla", 2020),
			Auto("Mercedes-Benz", "Clase G", 2025)]

	def darBienvenida(self):
		print(self.mensajeDeBienvenida)

	def despliegaMenu(self):
		print("Las opciones son:")
		print("1. Ver modelos disponibles")
		print("2. Salir")
		opcion = input("Tecleaste la opcion:")
		return opcion
		
	def procesaOpcion(self, opcion):
		if(opcion == "1"):
			print("Estos son los autos disponibles:")
			for auto in self.autos:
				print(auto)

		elif(opcion == "2"):
			print("Saliendo del sistema...")
			return False
		
		else:
			print("Opción invalido")

		return True
		
