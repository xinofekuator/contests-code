package gcj;
import java.util.*;
import java.io.*;

public class SpeakingInTongues {
	final static String PROBLEM_NAME="tongue";
	final static String DIR="C:\\Users\\xino\\Desktop\\GCJ\\" + PROBLEM_NAME +"\\";

	static char[] code=new char[26];
	static void preprocess(){
		String in="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
		String out="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
		
		Arrays.fill(code,'?');
		for(int i=0;i<=in.length()-1;i++){
			if(in.charAt(i)!=' '){
				code[in.charAt(i)-'a']=out.charAt(i);
			}
		}
		for(int i=0;i<=code.length-1;i++){
			System.out.println((char) ((int)'a'+ i) +" == > "+code[i]);
		}
		code['z'-'a']='q';
		code['q'-'a']='z';
	}
	void solve(PrintWriter pw,Scanner sc){
		String s=sc.nextLine();
		for(char c:s.toCharArray()){
			if(c==' '){
				pw.print(c);
			}
			else{
				pw.print(code[c-'a']);
			}
		}
		pw.println();
	}
	public static void main(String[] args) throws Exception{
		preprocess();
		Scanner sc= new Scanner(new FileReader(DIR+"input.txt"));
		PrintWriter pw=new PrintWriter(new FileWriter(DIR+"output.txt"));
		int caseInt=sc.nextInt();
		sc.nextLine();
		for(int i=1;i<=caseInt;i++){
			System.out.println("Processing case"+i);
			pw.print("Case #"+i+": ");
			new SpeakingInTongues().solve(pw, sc);
		}
		pw.flush();
		pw.close();
		sc.close();
	}
}
