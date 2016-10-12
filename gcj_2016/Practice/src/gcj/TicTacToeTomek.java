package gcj;
import java.util.*;
import java.io.*;

public class TicTacToeTomek {
	final static String PROBLEM_NAME="tictac";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";
	static Scanner sc;
	static char[][] datos=new char[4][4];
	static String[] respuestas={"X won","O won","Draw","Game has not completed"};

	void preprocess(){
		for(int i=0;i<4;i++){
			String in=sc.nextLine();
			char[] a=in.toCharArray();
			for(int j=0;j<4;j++){
				datos[i][j]=a[j];
			}
		}
	}
	boolean ganaHorizontal(char dato){
		boolean resultado=false;
		boolean terminado1=false;

		for(int i=0;i<4 && !terminado1;i++){
			boolean terminado2=false;
			for(int j=0;j<4 && !terminado2;j++){
				if(datos[i][j]!=dato && datos[i][j]!='T'){
					terminado2=true;
				}
			}
			if(terminado2==false){
				resultado=true;
				terminado1=true;
			}
		}
		return resultado;
	}

	boolean ganaVertical(char dato){
		boolean resultado=false;
		boolean terminado1=false;

		for(int i=0;i<4 && !terminado1;i++){
			boolean terminado2=false;
			for(int j=0;j<4 && !terminado2;j++){
				if(datos[j][i]!=dato && datos[j][i]!='T'){
					terminado2=true;
				}
			}
			if(terminado2==false){
				resultado=true;
				terminado1=true;
			}
		}
		return resultado;
	}
	
	boolean ganaDiagonal1(char dato){
		boolean resultado=false;
		boolean isPosible=true;
		for(int i=0;i<4 && isPosible;i++){
			if(datos[i][i]!=dato && datos[i][i]!='T'){
				isPosible=false;
			}
		}
		if(isPosible==true){
			resultado=true;
		}
		return resultado;
	}
	boolean ganaDiagonal2(char dato){
		boolean resultado=false;
		boolean isPosible=true;
		int contador=3;
		for(int i=0;i<4 && isPosible;i++){
			if(datos[contador][i]!=dato && datos[contador][i]!='T'){
				isPosible=false;
			}
			contador--;
		}

		if(isPosible==true){
			resultado=true;
		}
		return resultado;
	}

	boolean tableroLleno(){
		boolean terminado=false;
		boolean solucion=true;
		for(int i=0;i<4 && !terminado;i++){
			for(int j=0;j<4 && !terminado;j++){
				if(datos[i][j]=='.'){
					terminado=true;
				}
			}
		}
		if(terminado==true){
			solucion=false;
		}
		return solucion; 
	}

	void solve(PrintWriter pw,Scanner sc){
		this.preprocess();
		String solucion;
		if(ganaHorizontal('X') || ganaVertical('X') || ganaDiagonal1('X') || ganaDiagonal2('X')){
			solucion=respuestas[0];
		}
		else if(ganaHorizontal('O') || ganaVertical('O') || ganaDiagonal1('O') || ganaDiagonal2('O')){
			solucion=respuestas[1];
		}
		else if(tableroLleno()==true){
			solucion=respuestas[2];
		}
		else{
			solucion=respuestas[3];
		}

		pw.print(solucion);
		sc.nextLine();
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
			new TicTacToeTomek().solve(pw, sc);
			TicTacToeTomek a=new TicTacToeTomek();
		}
		pw.flush();
		pw.close();
		sc.close();

	}	
}


