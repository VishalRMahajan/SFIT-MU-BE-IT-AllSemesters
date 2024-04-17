import java.util.Scanner;

/*
   Condition for leap year is if leap is divisible by 4 and not by 100 its leap year
   if leap year is divisible by 100 but not by 400 then its not leap year and
   if the leap year is divisble by 400 then it is a leap year
 */
public class leapyear{
    public static void main(String[] args) {
        
        System.out.print("Enter the year: ");
        Scanner sc= new Scanner(System.in);
        int year = sc.nextInt();

        boolean isLeap;

        if (year % 4 == 0) //1st condition
        {
            if (year % 100 == 0)//second condition
            {
                if (year % 400 == 0)//third condition
                {
                    isLeap = true;
                } 
                else 
                {
                    isLeap = false;
                }
            } 
            else 
            {
                isLeap = true;
            }
        }
        else 
        {
            isLeap = false;
        }

        if (isLeap) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }
    }
}