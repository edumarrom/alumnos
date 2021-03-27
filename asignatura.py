class Asignatura:
	"""
	Representa una asignatura, identificada por su denominación.
	"""
	def __init__(self, denominacion, num_trim):
		self.__set_denom(denominacion)
		self.__set_num_trimestres(num_trim)

	def __repr__(self):
		return f"Asignatura('{self.denom()}', {self.num_trimestres()})"

	def __str__(self):
		return f'Es la asignatura {self.denom()}, que consta de {self.num_trimestres()} trimestre(s).'

	def denom(self):
		return self.__denom

	def num_trimestres(self):
		return self.__num_trimestres

	def __set_denom(self, denominacion):
		self.__denom = denominacion

	def __set_num_trimestres(self, num_trim):
		self.__num_trimestres = num_trim
