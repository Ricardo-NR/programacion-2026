''' 
Creado en Febrero del 2026 
@autor: Ricardo-NR

'''
class Cuenta:

	# por ahora nuestra clase sólo tiene un atributo.
	def __init__(self, valor, tipo):
		self.cantidad = valor
		self.tipo = tipo

	#informacion
	def imprimirDetalles(self):
		print(self.cantidad)
		print(self.tipo)

	def retirar(self, cantidad):
		self.cantidad = self.cantidad - cantidad 

	def depositar(self, cantidad):
		self.cantidad = self.cantidad +cantidad 