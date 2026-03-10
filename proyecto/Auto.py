''' 
 Crado en Marzo del 2026
@autor: Ricardo-NR
'''

class Auto:
	
	def __init__(self, marca, modelo, año):
		self.marca = marca
		self.modelo = modelo
		self.año = año

	# informacion
	def imprimirDetalles(self):
		print(self.marca)
		print(self.modelo)
		print(self.año)

	def cambiarModelo(self, modelo):
		self.modelo = modelo

	def cambiarAño(self, año):
		self.año = año