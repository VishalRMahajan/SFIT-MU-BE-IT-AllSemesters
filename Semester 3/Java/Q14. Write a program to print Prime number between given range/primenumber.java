import java.util.Scanner;

public class primenumber
{
    public static void main(String[] args)
    {   
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter the Lower Limit: ");
        int lower= sc.nextInt();

        System.out.print("Enter the Upper Limit: ");
        int upper= sc.nextInt();

        if(lower >= 2 || upper >=2 && lower<upper)
            primenumberprint(lower, upper);
        else
            System.out.println("Enter Valid Limits");

        sc.close();
       
    }

    public static void primenumberprint(int lower,int upper)
    {   
        
        for (int num= lower; num<=upper;num++)
        {
            int count=0;

            for(int i=1;i<=upper;i++)
            {
                if(num%i==0)
                    count++;
            }

            if(count==2)
                System.out.print(num +" ");
        }
      
    }
}