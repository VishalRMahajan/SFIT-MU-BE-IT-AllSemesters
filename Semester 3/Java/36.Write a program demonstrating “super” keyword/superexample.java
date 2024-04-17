class Parent
{
    String Name = "vishal";
}

class Child extends Parent
{
    void accessSuper()
    {
        System.out.println("Name in Parent Class is "+ super.Name);
    }
}

public class superexample {
    public static void main(String[] args) {
        Child child = new Child();
        child.accessSuper();
    }
}