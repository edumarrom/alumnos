from asignatura import Asignatura
from alumno import Alumno

class Principal:

	def __init__(self):
		ingles = Asignatura('Ingles', 3)
		paco = Alumno('Paco', 'B')
		paco.matricular(ingles)
		print(paco)
		input('Presiona Intro para finalizar.')
