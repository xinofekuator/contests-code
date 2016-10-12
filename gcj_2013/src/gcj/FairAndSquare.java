package gcj;
import java.util.*;
import java.io.*;
import java.math.*;

public class FairAndSquare {
	final static String PROBLEM_NAME="fairsquare";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";
	
	static boolean isPalindrome(String s){
		boolean terminado=false;
		char[] cadena=s.toCharArray();
		int len=s.length();
		for(int i=0,j=len-1;i<=j && !terminado;i++,j--){
			if(cadena[i]!=cadena[j]){
				terminado=true;
			}
		}
		return !terminado;
	}
	
	static boolean isPalindrome(BigInteger a ){
		return isPalindrome(a.toString());
	}
	
	static public BigDecimal getRaizBigDecimal(String numero, int precision) {

        BigDecimal bigNumero = new BigDecimal(numero);

        BigDecimal raiz = BigDecimal.ONE;
        BigDecimal raizTemp = null;

        if (bigNumero.compareTo(BigDecimal.ZERO) < 1) {
            System.err.println("ERROR");
            return BigDecimal.ZERO;
        }

        for (int i = 0; i < precision; i++) {
            raizTemp = raiz;
            raiz = raiz.pow(2).subtract(bigNumero);
            raiz = raiz.divide(raizTemp.multiply(BigDecimal.valueOf(2)), 10,
            		RoundingMode.HALF_UP);

            raiz = raizTemp.subtract(raiz);
        }
        return raiz;
    }
	
	
	static BigDecimal limiteInf(BigInteger a){
		BigDecimal resultado=BigDecimal.ZERO;
		BigDecimal b=new BigDecimal(a);
		BigDecimal raiz=getRaizBigDecimal(b.toString(),400);	
		BigDecimal truncado=raiz.setScale(0, RoundingMode.CEILING);
		if((raiz.subtract(truncado)).compareTo(new BigDecimal("0.000001"))>1){
			resultado=truncado.add(BigDecimal.ONE);
		}
		else{
			resultado=truncado;
		}
		return resultado;
	}
	static BigDecimal limiteSup(BigInteger a){
		BigDecimal resultado=BigDecimal.ZERO;
		BigDecimal b=new BigDecimal(a);
		BigDecimal raiz=getRaizBigDecimal(b.toString(),400);	
		BigDecimal truncado=raiz.setScale(0, RoundingMode.FLOOR);
		if((raiz.subtract(truncado)).compareTo(new BigDecimal("0.000001"))>1){
			resultado=truncado.add(BigDecimal.ONE);
		}
		else{
			resultado=truncado;
		}
		return resultado;
	}

	
	void solve(PrintWriter pw,Scanner sc){
		BigInteger a=sc.nextBigInteger();
		BigInteger b=sc.nextBigInteger();
		BigInteger inf=limiteInf(a).toBigInteger();
		BigInteger sup=limiteSup(b).toBigInteger();
		int solucion=0;
		for(BigInteger i=inf;i.compareTo(sup)<=0;i=i.add(BigInteger.ONE)){
			//System.out.println(i+" ");
			//System.out.println(i.pow(2));
			if(isPalindrome(i)&&isPalindrome(i.pow(2))){
				solucion++;
			}
		}
		
		pw.print(solucion);
		sc.nextLine();
		pw.println();
	}

	public static void main(String[] args) throws Exception{
		//System.out.print(new BigInteger("0").add(BigInteger.ONE));
		//System.out.print(new BigInteger("3").compareTo(new BigInteger("2")));
		//System.out.print(isPalindrome(new BigInteger("2").pow(2)));
		Scanner sc= new Scanner(new FileReader(DIR+"input.txt"));
		PrintWriter pw=new PrintWriter(new FileWriter(DIR+"output.txt"));
		int caseInt=sc.nextInt();
		sc.nextLine();
		for(int i=1;i<=caseInt;i++){
			System.out.println("Processing case"+i);
			pw.print("Case #"+i+": ");
			new FairAndSquare().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();
	
	}
}
