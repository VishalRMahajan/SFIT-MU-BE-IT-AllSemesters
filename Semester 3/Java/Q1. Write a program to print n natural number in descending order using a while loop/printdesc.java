import java.util.Scanner;

public class printdesc 
{
    public static void main(String[] args)
    {
        System.out.print("Enter the numbers from which to print: ");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        
        System.out.print("Number in Descending order is: ");
        for(int i=n;i>=1;i--)
        {
            System.out.print(i + " ");
          

        }

    }
}
