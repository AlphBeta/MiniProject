import java.util.*;

class Run extends Thread{
 String s;
 Run(String t){
	this.s=t;
 }
 public void run(){
	try{
		new MyFrame(this.s);
	}
	catch(Exception e){
	System.out.print(e);
	}
 }
}

public class Main {
 public static void main(String[] args) {
	int c,i;
	Scanner sc = new Scanner(System.in);
	Scanner scc = new Scanner(System.in);
	System.out.print("How many:");
	c=sc.nextInt();
	String s[] = new String[10];
	String t[] = new String[10];
	Run r[] = new Run[10];
	for(i =0;i<c;i++){
	s[i]=new String();
	t[i]=new String();
	System.out.print("Continent:");
	s[i]=scc.nextLine();
	System.out.print("Capital/Place:");
	t[i]=scc.nextLine();
	}
	for(i = 0;i<c;i++){
	r[i] = new Run(s[i]+"/"+t[i]);
	}
	for(i=0;i<c;i++)
		r[i].start();
 }
}

