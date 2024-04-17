interface Parent1
{
    void method1();
}

interface Parent2
{
    void method2();
}

class child implements Parent1,Parent2
{
    public void method1()
    {
        System.out.println("This is method 1");
    }

    public void method2()
    {
        System.out.println("This is method 2");
    }

}

public class inheritanceexample
{
    public static void main(String[] args) {
        child child = new child();
        child.method1();
        child.method2();
    }
}


