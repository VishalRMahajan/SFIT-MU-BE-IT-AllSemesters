import java.util.Scanner;

public class largestofthree
{
    public static void main(String[] args)
    {
        int Num1,Num2,Num3;
        System.out.print("Enter the three Number sepearted by spaces: ");

        Scanner sc= new Scanner(System.in);

        Num1=sc.nextInt();
        Num2=sc.nextInt();
        Num3=sc.nextInt();

        int largest;

        if(Num1>Num2)
        {
            if(Num1>Num3)
                largest=Num1;
            else
                largest=Num3;
        }
        else
        {
            if(Num2>Num3)
                largest=Num2;
            else
                largest=Num3;
        }

        System.out.print("Largest of Three Numbers "+Num1+ " " + Num2 +" "+ Num3 + " = " + largest);
    }
}