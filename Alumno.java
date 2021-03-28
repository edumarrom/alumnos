import java.util.HashSet;
import java.util.stream.IntStream;
import java.util.HashMap;

/**
 * Representa a un alumno, el cual se identifica
 * por su nombre y grupo.
 */
public class Alumno{
    private String nombre;
    private int grupo;
    private HashSet<Asignatura> asignaturas = new HashSet<Asignatura>();
    private HashMap<String, Double> notas = new HashMap<String, Double>();
    private String trims = "";  // No entiendo...
    /**
     * Constructor de la clase Alumno.
     */
    public Alumno(String nombre, int grupo){
          this.setNombre(nombre);
          this.setGrupo(grupo);
    }

    /*
     * def __repr__(self):
     *    """Devuelve la forma normal de la asignatura."""
     *    return f"Asignatura('{self.denom()}', {self.num_trimestres()})"
     */

    /**
     * Devuelve un literal de cadena que representa al alumno.
     * @return La representación literal del alumno.
     */
    public String toString(){
          return "Soy el alumno " + this.nombre() + ", y pertenezco al " + this.grupo() + ".";
    }

    /**
     * Devuelve el nombre del alumno.
     * @return El nombre Eel alumno.
     */
    public String nombre(){
          return this.nombre;
    }

    /**
     * Devuelve el grupo del alumno.
     * @returnEl grupo del alumno.
     */
    public int grupo(){
          return this.grupo;
    }

    /**
     * Devuelve la lista de asignaturas del alumno.
     * @return La lista de asignaturas del alumno.
     */
    private HashSet<Asignatura> asignaturas(){
        return this.asignaturas;
    }

    /**
     * Devuelve las notas del alumno.
     * @return Las notas del alumno.
     */
    private HashMap<String, Double> notas(){
        return this.notas;
    }

    /**
     * Asigna un nombre al alumno.
     * @param nombre El nuevo nombre.
     */
    private void setNombre(String nombre){
        this.nombre = nombre;
    }

    /**
     * Asigna un grupo al alumno.
     * @param grupo El nuevo grupo.
     */
    private void setGrupo(int grupo){
        this.grupo = grupo;
    }

    /**
     * Asigna una asignatura a la lista de asignaturas
     * del alumno.
     * @param asignatura La nueva asignatura.
     */
    private void setAsignatura(Asignatura asignatura){
        this.asignaturas.add(asignatura);
    }

    /**
     * Asigna una nota al trimestre de una asignatura.
     * @param asignatura La asignatura a la que asignar la nota.
     * @param trimestre El trimestre al que asignar la nota.
     * @param nota La nueva nota.
     * @return El propio objeto Alumno.
     */
    public Alumno setNota(Asignatura asignatura, int trimestre, Double nota){
        trims = "";
        IntStream.rangeClosed(1, asignatura.numTrimestres()).forEach(t -> trims += String.valueOf(t));
        if(trims.contains(String.valueOf(trimestre))){
            String clave = asignatura.denom() + String.valueOf(trimestre);
            this.notas.put(clave, nota);
        }
        return this;
    }

    /**
     * Matricula a un alumno en una asignatura.
     * @param asignatura La asignatura en la que matricular.
     * @return Mel propio objeto Alumno.
     */
    public Alumno matricular(Asignatura asignatura){
        this.setAsignatura(asignatura);
        return this;
    }

    /**
     * Devuelve la nota de un trimestre y asignatura en concreto, null si la nota no existe.
     * @param asignatura La asignatura a consultar.
     * @param trimestre La nota a consultar.
     * @return La nota del trimestre y asignatura en concreto.
     */
    public Double nota(Asignatura asignatura, int trimestre){
        String clave = asignatura.denom() + String.valueOf(trimestre);
            return this.notas().get(clave);
    }

    /**
     * Devuelve la nota media del alumno en una asignatura.
     * @param asignatura La asignatura a consultar.
     * @return La nota media del alumno en una asignatura.
     */
    public Double media(Asignatura asignatura){
        Double media = 0.0;
        if(this.asignaturas().contains(asignatura)){
            for(int t = 1; t <= asignatura.numTrimestres(); t ++){
                if(this.nota(asignatura, t) == null){
                    media += 0;
                }else{
                    media += this.nota(asignatura, t);
                }
            }
        }
        return media / asignatura.numTrimestres();
    }

    /**
     * Devuelve True si la media del alumno en una
     * asignatura es igual o mayor que 5, False en
     * caso contrario.
     * @param asignatura La asignatura a consultar.
     * @return True si la media es mayor o igual que 5, false en caso contrario.
     */
    public boolean aprobada(Asignatura asignatura){
        boolean aprobado = false;
        if(this.media(asignatura) >= 5.0){
            aprobado = true;
        }
        return aprobado;
    }
}
