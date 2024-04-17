import java.util.Scanner;

class rectangle
{
	public  double length;
	public  double breadth;
	
	public rectangle(double length,double breadth)
	{
	    this.length=length;
	    this.breadth=breadth;
	}

	public  double calculatearea()
	{
	   return length*breadth;
	}
	
}

public class areausingconstructor
{
	public static void main(String[] args)
	{
	    Scanner sc=new Scanner(System.in);

	    System.out.print("Enter the length of rectangle: ");
	    double length= sc.nextDouble();

	    System.out.print("Enter the Breadth of rectangle: ");
	    double breadth= sc.nextDouble();
	
	    rectangle rc= new rectangle(length ,breadth);
	    
	    double area = rc.calculatearea();

	    System.out.print("Area of Rectangle with Length "+length + " and breadth "+ breadth +" is " + area);
	    
	}
}