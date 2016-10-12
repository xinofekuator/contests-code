package gcj;
import java.util.*;
import java.io.*;

public class Lawnmower {
	final static String PROBLEM_NAME="lawn";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";
	static Scanner sc;
	static char[][] datos;
	static String[] respuestas={"YES","NO"};
	int n;
	int m;

	void preprocess(){
		n=sc.nextInt();
		m=sc.nextInt();
		datos=new char[n][m];
		sc.nextLine();
		for(int i=0;i<n;i++){
			String in=sc.nextLine();
			char[] a=new char[m];
			int contador=0;
			for(int c=0;c<=in.length()-1;c++){
				if(in.charAt(c)!=' '){
					a[contador]=in.charAt(c);
					contador++;
				}
			for(int j=0;j<m;j++){
					datos[i][j]=a[j];
				}
			}
		}
	}

	void cortadoHorizontal(char dato){
		for(int i=0;i<n;i++){
			boolean terminado=false;
			for(int j=0;j<m && !terminado;j++){
				if(datos[i][j]!=dato && datos[i][j]!='T'){
					terminado=true;
				}
			}
			for(int j=0;j<m && !terminado;j++){
				datos[i][j]='T';
			}
		}
	}
		

	void cortadoVertical(char dato){
		for(int j=0;j<m;j++){
			boolean terminado=false;
			for(int i=0;i<n && !terminado;i++){
				if(datos[i][j]!=dato && datos[i][j]!='T'){
					terminado=true;
				}
			}
			for(int i=0;i<n && !terminado;i++){
				datos[i][j]='T';
			}
		}
	}

	boolean buscar(char a){
		boolean resultado=true;
		boolean terminado=false;
		for(int i=0;i<n && !terminado;i++){
			for(int j=0;j<m && !terminado;j++){
				if(datos[i][j]==a){
					terminado=true;
				}
			}
		}
		resultado=!terminado;
		return resultado;
	}


	void solve(PrintWriter pw,Scanner sc){
		this.preprocess();
		String solucion;
		this.cortadoHorizontal('1');
		this.cortadoVertical('1');
		if(buscar('1')){
			solucion=respuestas[0];
		}
		else {
			solucion=respuestas[1];
		}
		pw.print(solucion);
		pw.println();
	}

	public static void main(String[] args) throws Exception{
		sc= new Scanner(new FileReader(DIR+"input.txt"));
		PrintWriter pw=new PrintWriter(new FileWriter(DIR+"output.txt"));
		int caseInt=sc.nextInt();
		sc.nextLine();
		for(int i=1;i<=caseInt;i++){
			System.out.println("Processing case"+i);
			pw.print("Case #"+i+": ");
			new Lawnmower().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();

	}	
}


