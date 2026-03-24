''' 
Creado en Marzo del 2026
@autor: Ricardo-NR
'''

class Auto:
	
	def __init__(self, marca, modelo, año):
		self.marca = marca
		self.modelo = modelo
		self.año = año

	def cambiarModelo(self, modelo):
		if modelo:
			self.modelo = modelo
			return True
		return False

	def cambiarAño(self, año):
		if año > 1900:
			self.año = año
			return True
		return False

	def __str__(self):
		return f"{self.marca} | {self.modelo} | {self.año}"
