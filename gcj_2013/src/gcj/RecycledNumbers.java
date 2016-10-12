package gcj;
import java.util.*;
import java.io.*;
import java.math.*;

public class RecycledNumbers {
	final static String PROBLEM_NAME="numbers";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";

	private int reciclados(int n,int lim){
		Integer numero=(Integer)n;
		String num=numero.toString();
		int len=num.length();
		int resultado=0;
		
		for(int i=1;i<len;i++){
			int div=(int)Math.pow(10, i);
			int mult=(int)Math.pow(10, len-i);
			int aux=(n/div)+((n%div)*mult);
			if(aux==n){
				break;
			}
			if(aux<=lim && aux>=n){
				resultado++;
			}
		}
		return resultado;
	}

	void solve(PrintWriter pw,Scanner sc){
		int a=sc.nextInt();
		int b=sc.nextInt();
		int solucion=0;
		for(int i=a;i<b;i++){
			solucion=solucion+reciclados(i,b);
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
			new RecycledNumbers().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();

	}	
}


