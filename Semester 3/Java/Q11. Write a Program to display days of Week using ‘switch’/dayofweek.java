import java.util.Scanner;

public class dayofweek {
    public static void main(String[] args)
     {

        int loop = 1;

        while (loop == 1)
         {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter the Day of week: ");
            int choice = sc.nextInt();

            switch (choice)
             {
                case 1:
                    System.out.print(choice +"st day of the week is Sunday ");
                    break;

                case 2:
                    System.out.print(choice +"nd day of the week is Monday ");
                    break;

                case 3:
                    System.out.print(choice +"rd day of the week is Tuesday ");
                    break;

                case 4:
                    System.out.print(choice +"th day of the week is Wednesday ");
                    break;

                case 5:
                    System.out.print(choice +"th day of the week is Thursday ");
                    break;

                case 6:
                    System.out.print(choice +"th day of the week is Friday ");
                    break;

                case 7:
                    System.out.print(choice +"th day of the week is Saturday ");
                    break;

                default:
                    System.out.print("Week only have 7 days !! Input option from 1 to 7 ");
            }

            System.out.print("\n Do you want to Continue(1 for Yes): ");
            loop= sc.nextInt();
        }
    }

}