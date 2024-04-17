//Write a program that accepts radius and returns the area of a circle using function call

import java.util.Scanner;

public class area {

     public static double calculateArea (double radius)
     {  
        double area;
        area= Math.PI *radius*radius;
        return area;
     }

     public static void main(String [] args)
     {
        System.out.print("Enter the radius of circle: ");
        Scanner sc= new Scanner(System.in);
        double radius= sc.nextDouble();

        double area=calculateArea(radius);

        System.out.print("Area of Circle with radius "+ radius +" is "+ area);
     }
}