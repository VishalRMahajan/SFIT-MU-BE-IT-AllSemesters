import java.util.Scanner;



public class larger
{   
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter the First Number: ");
        double Num1 = sc.nextDouble();

        System.out.print("Enter the Second Number: ");
        double Num2 = sc.nextDouble();

        double largest = largestoftwo(Num1,Num2);

        System.out.print("Largest of "+ Num1 +" and "+ Num2 +" is "+ largest);
    }

    private static double largestoftwo(double Num1, double Num2) 
    {
        if(Num1>Num2)
        {
            return Num1;
        }
        else
        {
            return Num2;
        }

    }

}