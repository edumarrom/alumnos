from asignatura import Asignatura
from alumno import Alumno

class Principal:

	def __init__(self):
		ingles = Asignatura('Inglés', 3)
		mates = Asignatura('Matemáticas', 2)
		juan = Alumno('Juan Pérez', 2).matricular(ingles).matricular(mates)
		juan.set_nota(ingles, 1, 4.0).set_nota(ingles, 2, 6.0).set_nota(ingles, 3, 8.0)
		antonio = Alumno('Antonio García').matricular(mates)
		antonio.set_nota(mates, 1, 2.5)
		print('	<---TESTS--->	')
		print(f'juan.media(ingles) == {juan.media(ingles)}')
		print(f'antonio.nota(mates, 2) == {antonio.nota(mates, 2)}')
		print(f'antonio.nota(mates, 1) == {antonio.nota(mates, 1)}')
		print(f'juan.aprobada(ingles) == {juan.aprobada(ingles)}')
		input('Presiona Intro para finalizar.')

if __name__ == '__main__':
	Principal()
