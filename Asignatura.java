/**
 * Representa una asignatura, identificada por su \
 * denominación y nº de trimestres.
 */
public class Asignatura{
  private String denom;
  private int numTrimestres;
  /**
   * Constructor de la clase Asignatura.
   */
  Asignatura(String denom, int numTrim){
		this.setDenom(denom);
		this.setNumTrimestres(numTrim);
    }

  /*
	def __repr__(self):
		"""Devuelve la forma normal de la asignatura."""
		return f"Asignatura('{self.denom()}', {self.num_trimestres()})"
  */

  /**
   * Devuelve un literal de cadena que representa a la asignatura.
   * @return La representación literal del alumno.
   */
	public String toString(){
		return "Es la asignatura " + this.denom() + ", que consta de " + this.numTrimestres() + " trimestre(s).";
    }

  /**
   * Devuelve la denominación de la asignatura.
   * @return La denominación de la asignatura.
   */
	public String denom(){
		return this.denom;
    }

  /**
   * Devuelve el nº de trimestres de la asignatura.
   */
	public int numTrimestres(){
		return this.numTrimestres;
    }

  /**
   * Asigna una denominación a la asignatura.
   * @param denom La nueva denominación.
   */
	private void setDenom(String denom){
		this.denom = denom;
    }

  /**
   * Asigna un nº de trimestres a la asignatura.
   * @param numTrim El nuevo nº de trimestres.
   */
	private void setNumTrimestres(int numTrim){
		this.numTrimestres = numTrim;
    }
}
