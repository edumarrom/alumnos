class Alumno:
	"""
	Representa a un alumno, el cual se identifica \
    	por su nombre y grupo.
	"""

	def __init__(self, nombre, grupo = 1):
		"""Constructor de la clase Alumno."""
		self.__set_nombre(nombre)
		self.__set_grupo(grupo)
		self.__asignaturas = set()
		self.__notas = {}

	def __str__(self):
		"""Devuelve un literal de cadena que representa \
      		al Alumno."""
		return f'Soy el alumno {self.nombre()}, y pertenezco al grupo '\
      		f'{self.grupo()}.'

	def nombre(self):
		"""Devuelve el nombre del alumno."""
		return self.__nombre

	def grupo(self):
		"""Devuelve el grupo del alumno."""
		return self.__grupo

	def __get_asignaturas(self):
		"""Devuelve las asignaturas del alumno."""
		return self.__asignaturas

	def __get_notas(self):
		"""Devuelve las notas del alumno."""
		return self.__notas

	def __set_nombre(self, nombre):
		"""
  		Asigna un nombre al alumno.

		Recibe:
			- nombre: int -> El nuevo nombre.
    	"""
		self.__nombre = nombre

	def __set_grupo(self, grupo):
		"""
  		Asigna un grupo al alumno.

		Recibe:
			- grupo: int -> El nuevo grupo.
     	"""
		self.__grupo = grupo

	def __set_asignatura(self, asignatura):
		"""
  		Asigna una asignatura a la lista de asignaturas \
        	del alumno.

		Recibe:
  			- asignatura: Asignatura -> La nueva asignatura.

  		Un alumno no puede estar matriculado en una \
      		asignatura más de una vez.
		"""
		self.__asignaturas.add(asignatura)

	def set_nota(self, asignatura, trimestre, nota):
		"""
		Asigna una nota al trimestre de una asignatura.

		Recibe:
			- asignatura: Asignatura -> La asignatura a la \
       			que asignar la nota.
			- trimestre: int -> El trimestre al \
       			que asignar la nota.
			- nota: float -> La nueva nota.

        Devuelve el propio objeto Alumno.

		Si el trimestre recibido supera el nº de trimestres \
			de la asignatura, devuelve una excepción \
       		ValueError.
		"""
		if trimestre in range(asignatura.num_trimestres() + 1):
			clave = (asignatura, trimestre)
			self.__notas[clave] = nota
		else: raise ValueError(f'{asignatura.denom()} sólo tiene {asignatura.num_trimestres()} trimestres.')
		return self

	def matricular(self, asignatura):
		"""Matricula a un alumno en una asignatura."""
		self.__set_asignatura(asignatura)
		return self

	def nota(self, asignatura, trimestre):
		"""
  		Devuelve la nota de un trimestre y asignatura \
        	en concreto, None si esa nota no existe.
		"""
		clave = (asignatura, trimestre)
		for k in self.__get_notas().keys():
			if k == clave:
				return self.__get_notas().get(clave)

	def media(self, asignatura):
		"""
  		Devuelve la nota media del alumno en una asignatura.
		"""
		if asignatura in self.__get_asignaturas():
			notas = 0
			for t in range(asignatura.num_trimestres() + 1):
				if self.nota(asignatura, t) == None:
					notas += 0
				else: notas += self.nota(asignatura, t)
			return notas / asignatura.num_trimestres()
		else: raise ValueError(f'{self.nombre()} no está matriculado en {asignatura.denom()}.')

	def aprobada(self, asignatura):
		"""
  		Devuelve True si la media del alumno en una \
        	asignatura es igual o mayor que 5, False en \
            caso contrario.
        """
		return True if self.media(asignatura) >= 5 else False
