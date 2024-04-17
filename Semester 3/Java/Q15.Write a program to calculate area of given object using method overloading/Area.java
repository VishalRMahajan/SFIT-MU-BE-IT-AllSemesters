import java.util.Scanner;

public class Area
{
    public static void main(String[] args)
    {
        System.out.println("+--------MENU-------+ ");
        System.out.println("|  1.Rectangle      | ");
        System.out.println("|  2.Circle         | ");
        System.out.println("|  3.Triange        | ");
        System.out.println("+-------------------+ ");

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Choice: ");
        int choice = sc.nextInt();

        switch(choice)
        {
            case 1:
            System.out.print("Enter the length of Rectangle: ");
            double length= sc.nextDouble();

            System.out.print("Enter the breadth of Rectangle: ");
            double breadth= sc.nextDouble();

            double rectangle = rectangle(length, breadth);

            System.out.println("Area of rectangle with "+length +" and "+ breadth + " is " + rectangle);

            break;

            case 2:
            System.out.print("Enter the radius of circle: ");
            double radius= sc.nextDouble();

            double circle = circle(radius);

            System.out.println("Area od Circle with "+ radius + " is "+ circle);

            break;

            case 3:
            System.out.print("Enter the base of Triangle: ");
            double base= sc.nextDouble();

            System.out.print("Enter the height of Triangle: ");
            double height= sc.nextDouble();

            double triangle = triangle(base, height);
            System.out.println("Area of Triangle with "+ base + " and " + height + " is "+ triangle);
            break;

            default:
             System.out.print("Enter Valid Choice!! ");
            break;


            


        }

            sc.close();

        


    }

    public static double rectangle(double length,double breadth)
    {
        return length * breadth;
    }

    public static double circle(double radius)
    {
        return Math.PI * radius *radius;
    }

    public static double triangle(double base,double height)
    {
        return 0.5*base*height;
    }
}