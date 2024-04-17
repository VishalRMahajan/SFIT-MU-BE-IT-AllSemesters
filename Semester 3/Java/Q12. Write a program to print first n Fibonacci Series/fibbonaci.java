import java.util.Scanner;

public class fibbonaci
{
    public static void main(String[] args)
    {
        System.out.print("Enter the Number till which to print fibbonaci: ");
        Scanner sc= new Scanner(System.in);
        int limit= sc.nextInt();

        if(limit<=0)
            System.out.print("Enter positive Non zero Integer!!! ");
        else
            printfibonnaci(limit);
    }

    public static void printfibonnaci(int limit)
    {   
        int first=0,second=1;
        int fibbonaci;

        for(int i=1;i<=limit;i++)
        {
            System.out.print(first + " ");
            fibbonaci=first+second;
            first=second;
            second=fibbonaci;
        }
        
    }
}