import java.util.*;
import java.lang.*;
import java.io.*;

public class Exponent 
{
    public static void expo(int a,int b)
    {
        double n=Math.pow(a,b);
        System.out.println(Math.round(n));
    }
	public static void main (String[] args) 
	{
	    Exponent z=new Exponent();
	    Scanner sc=new Scanner(System.in);
	    int a=sc.nextInt();
	    int b=sc.nextInt();
	    z.expo(a,b);
	}
}
