package gcj;
import java.util.*;
import java.io.*;

public class Osmos {
	final static String PROBLEM_NAME="osmos";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";

	boolean comprobar(int numero,int objetivo,int numQuedan){
		int sol=numero;
		boolean resultado=false;
		for(int i=0;i<numQuedan;i++){
			sol=sol+sol-1;
		}
		if(sol>objetivo){
			resultado=true;
		}
		return resultado;
	}
	
	int[] pasos(int numero,int objetivo,int numQuedan){
		int[] pasos={0,0};
		int sol=numero;
		boolean terminado=false;
		for(int i=0;i<numQuedan && !terminado;i++){
			if(sol<=objetivo){
				sol=sol+sol-1;
				pasos[0]++;
			}
			else{
				terminado=true;
			}
		}
		pasos[1]=sol;
		return pasos;
	}
	
	void solve(PrintWriter pw,Scanner sc){
		int solucion=0;
		int myMote=sc.nextInt();
		int n=sc.nextInt();
		int[] motes=new int[n];
		for(int i=0;i<n;i++){
			motes[i]=sc.nextInt();
		}
		
		for(int a=1;a<n;a++){
			boolean terminado=false;
			for(int b=a;b>0 && !terminado;b--){
				if(motes[b]<motes[b-1]){
					int aux=motes[b-1];
					motes[b-1]=motes[b];
					motes[b]=aux;
				}
				else{
					terminado=true;
				}
			}
		}
		
		System.out.println(comprobar(myMote,motes[0],motes.length));
		System.out.println(pasos(myMote,motes[0],motes.length)[0]);
		System.out.println(pasos(myMote,motes[0],motes.length)[1]);
		System.out.print(myMote);
		
		boolean terminado=false;
		for(int c=0;c<n && !terminado;c++){
			if(myMote>motes[c]){
				myMote=myMote+motes[c];
			}
			else if((myMote+myMote-1)>motes[c]){
				myMote=myMote+myMote-1+motes[c];
				solucion++;
			}
			else if(comprobar(myMote,motes[c],motes.length-c)){
				int[] pasos=pasos(myMote,motes[c],motes.length-c);
				int numeroIteraciones=pasos[0];
				int numeroResult=pasos[1];
				solucion=solucion+numeroIteraciones;
				myMote=numeroResult;
			}
			else{
				terminado=true;
				solucion=solucion+motes.length-c;
			}
		}
		
		pw.print(solucion);
		sc.nextLine();
		pw.println();
	}


	public static void main(String[] args) throws Exception{

		Scanner sc= new Scanner(new FileReader(DIR+"input.txt"));
		PrintWriter pw=new PrintWriter(new FileWriter(DIR+"output.txt"));
		int caseInt=sc.nextInt();
		sc.nextLine();
		for(int i=1;i<=caseInt;i++){
			System.out.println("Processing case"+i);
			pw.print("Case #"+i+": ");
			new Osmos().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();

	}	
}
