class MedioDeTransporte:
	def __init__(self,combustible):
		#<elipsis-for-student@
		self.combustible = combustible
		#@elipsis-for-student>

	def cargar_combustible(self,combustible):
		#<elipsis-for-student@
		self.combustible += combustible
		#@elipsis-for-student>

	def entran_personas(self,pasajeros):
		#<elipsis-for-student@
		return self.maximo_personas() >= pasajeros
		#@elipsis-for-student>


	def maximo_personas(self):
		#<elipsis-for-student@
		return self.maximo_personas()
		#@elipsis-for-student>

class Auto(MedioDeTransporte):
	def maximo_personas(self):
		#<elipsis-for-student@
		return 5
		#@elipsis-for-student>

	def recorrer(self,kilometros):
		#<elipsis-for-student@
		self.litros -= kilometros / 2
		#@elipsis-for-student>

class Moto(MedioDeTransporte):
	def maximo_personas(self):
		#<elipsis-for-student@
		return 2
		#@elipsis-for-student>

	def recorrer(self,kilometros):
		#<elipsis-for-student@
		self.litros -= kilometros
		#@elipsis-for-student>


