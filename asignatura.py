class Asignatura:
	"""
	Representa una asignatura, identificada por su \
    	denominación y nº de trimestres.
	"""
	def __init__(self, denominacion, num_trim):
		"""Constructor de la clase Asignatura."""
		self.__set_denom(denominacion)
		self.__set_num_trimestres(num_trim)

	def __repr__(self):
		"""Devuelve la forma normal de la asignatura."""
		return f"Asignatura('{self.denom()}', {self.num_trimestres()})"

	def __str__(self):
		"""
  		Devuelve un literal de cadena que representa a la \
        	asignatura.
  		"""
		return f'Es la asignatura {self.denom()}, que consta de {self.num_trimestres()} trimestre(s).'

	def denom(self):
		"""Devuelve la denominación de la asignatura."""
		return self.__denom

	def num_trimestres(self):
		"""Devuelve el nº de trimestres de la asignatura."""
		return self.__num_trimestres

	def __set_denom(self, denominacion):
		"""
  		Asigna una denominación a la asignatura.

		Recibe:
			- denominacion: str -> La nueva denominación.
  		"""
		self.__denom = denominacion

	def __set_num_trimestres(self, num_trim):
		"""
  		Asigna un nº de trimestres a la asignatura.

		Recibe:
			- num_trim: str -> El nuevo nº de trimestres.
  		"""
		self.__num_trimestres = num_trim
