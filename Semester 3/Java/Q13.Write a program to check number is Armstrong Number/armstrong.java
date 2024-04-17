import java.util.Scanner;

public class armstrong {
    public static void main(String[] args)
     {
        System.out.print("Enter the Number to be Checked: ");
        Scanner sc = new Scanner(System.in);
        int original = sc.nextInt();

        int save = original;
        int unit = 0, temp = 0;

        while (save != 0) 
        {
            unit = save % 10;
            temp = temp + (unit * unit * unit);
            save = save / 10;
        }

        if(original==temp)
            System.out.println(original + " is a Armstrong Number");
        else
            System.out.println(original + " is not a Armstrong Number");
    }
}