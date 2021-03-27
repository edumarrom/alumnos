class Alumno:
	"""
	Representa a un alumno, el cual se identifica por su  nombre.
	"""
	def __init__(self, nombre, grupo):
		self.__set_nombre(nombre)
		self.__set_grupo(grupo)
		self.__asignaturas = []
		self.__notas = {}

	def __str__(self):
		return f'Soy el alumno {self.nombre()}, y pertenezco al grupo {self.grupo()}. '\
		f'Estoy matriculado en: {self.__get_asignaturas()}.'

	def nombre(self):
		return self.__nombre

	def grupo(self):
		return self.__grupo

	def __get_asignaturas(self):
		return self.__asignaturas

	def __get_notas(self):
		return self.__notas

	def __set_nombre(self, nombre):
		self.__nombre = nombre

	def __set_grupo(self, grupo):
		self.__grupo = grupo

	def __set_asignatura(self, asignatura):
		if asignatura not in self.__get_asignaturas():
			self.__asignaturas.append(asignatura)
		else: raise ValueError(f'{self.nombre()} ya está matriculado en {asignatura.denom()}.')

	def set_nota(self, asignatura, trimestre, nota):
		if asignatura in self.__get_asignaturas():
			clave = (asignatura, trimestre)
			self.__notas[clave] = nota
		else: raise ValueError('{self.nombre()} no está matriculado en {asignatura.denom()}.')

	def matricular(self, asignatura):
		self.__set_asignatura(asignatura)
		return self

	def nota(self, asignatura, trimestre):
		clave = (asignatura, trimestre)
		for k in self.__get_notas().keys():
			if k == clave:
				return self.__get_notas()[k]
