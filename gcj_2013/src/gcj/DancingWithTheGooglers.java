package gcj;
import java.util.*;
import java.io.*;

public class DancingWithTheGooglers {
	final static String PROBLEM_NAME="dance";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";
	
	//Return -1 if a surprising score is not possible
	
	private int surprising(int n){ 
		int resultado=-1;
		if(n==0||n==1||n==29||n==30){resultado=-1;}
		else{
			resultado=((n+1)/3)+1;
		}
		return resultado;
	} 
	private int unsurprising(int n){
		int resultado=-1;
		if(n==0){resultado=0;}
		else{
			resultado=((n-1)/3)+1;
		}
		return resultado;
	}
	

	void solve(PrintWriter pw,Scanner sc){
		int n=sc.nextInt();
		int sur=sc.nextInt();
		int note=sc.nextInt();
		int[] scores=new int[n];
		int solucion=0;
		int contador=sur;
		for(int i=0;i<n;i++){
			scores[i]=sc.nextInt();
			if(this.unsurprising(scores[i])>=note){
				solucion++;
			}
			else{
				if((this.surprising(scores[i])>=note)&&contador>0){
					solucion++;
					contador--;
				}
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
			new DancingWithTheGooglers().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();
		
	}	
}
