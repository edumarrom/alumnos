import java.util.Scanner;
public class Principal {
    public static Scanner in = new Scanner(System.in);
    public static void main(String[] args){
        Asignatura ingles = new Asignatura("Inglés", 3);
        Asignatura mates = new Asignatura("Matemáticas", 2);
        Alumno juan = new Alumno("Juan Pérez", 2).matricular(ingles).matricular(mates);
        juan.setNota(ingles, 1, 4.0).setNota(ingles, 2, 6.0).setNota(ingles, 3, 8.0);
        Alumno antonio = new Alumno("Antonio García", 1).matricular(mates);
        antonio.setNota(mates, 1, 2.5);
        System.out.println("	<---TESTS--->	");
		System.out.println("juan.media(ingles) == " + juan.media(ingles));
		System.out.println("antonio.nota(mates, 2) == " + antonio.nota(mates, 2));
		System.out.println("antonio.nota(mates, 1) == " + antonio.nota(mates, 1));
		System.out.println("juan.aprobada(ingles) == " + juan.aprobada(ingles));
        System.out.println("Presiona Intro para finalizar.");
		in.nextLine();
    }
}
