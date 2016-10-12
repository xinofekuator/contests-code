package gcj;
import java.util.*;
import java.io.*;
import java.math.*;

public class Bullseye {
	final static String PROBLEM_NAME="bullseye";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";

	BigInteger pinturaReq(BigInteger i){
		BigInteger a=BigInteger.ONE.add(BigInteger.ONE);
		return (i.multiply(a)).add(BigInteger.ONE);
	}

	void solve(PrintWriter pw,Scanner sc){
		BigInteger a=sc.nextBigInteger();
		BigInteger ml=sc.nextBigInteger();
		BigInteger sol=BigInteger.ZERO;
		BigInteger b=pinturaReq(a);
		while(ml.compareTo(b)>=0){

			a=a.add(BigInteger.ONE.add(BigInteger.ONE));
			ml=ml.subtract(b);
			sol=sol.add(BigInteger.ONE);
			b=pinturaReq(a);
		}

		pw.print(sol.toString());
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
			new Bullseye().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();

	}
}
