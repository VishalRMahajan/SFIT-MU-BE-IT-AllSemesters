/*19. Write a program for abstract class shape and abstract method draw. Create class rectangle and circle 
that will inherit method from Shape class. Make necessary assumptions */

abstract class Shape{
    abstract void draw();
}

class rectangle extends Shape
{
    void draw()
    {
        System.out.println("Drawing Rectangle");
    }
}

class circle extends Shape
{
    void draw()
    {
        System.out.println("Drawing Circle");
    }
}

public class Q19
{
    public static void main(String[] args)
    {
        rectangle rect = new rectangle();
        circle circle = new circle();

        rect.draw();
        circle.draw();
    }
}

