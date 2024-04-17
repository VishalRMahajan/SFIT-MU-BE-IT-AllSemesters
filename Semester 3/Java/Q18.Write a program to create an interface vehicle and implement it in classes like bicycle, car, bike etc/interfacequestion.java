interface vehicle
{
    void start();
    void wheels();
    void Stops();
}


class bicycle implements vehicle
{
    public void start()
    {
        System.out.println("bicycle Started");
    }

    public void wheels()
    {
        System.out.println("bicycle have 2 wheels");
    }

    public void Stops()
    {
        System.out.println("bicycle Stoped");
    }
}

class car implements vehicle
{
    public void start()
    {
        System.out.println("car Started");
    }

    public void wheels()
    {
        System.out.println("car have 4 wheels");
    }

    public void Stops()
    {
        System.out.println("car Stoped");
    }
}

class bike implements vehicle
{
    public void start()
    {
        System.out.println("bike Started");
    }

    public void wheels()
    {
        System.out.println("bike have 2 wheels");
    }

    public void Stops()
    {
        System.out.println("bike Stoped");
    }
}

public class interfacequestion
{
    public static void main(String[] args)
    {   
        bicycle bicycle= new bicycle();
        bicycle.start();
        bicycle.wheels();
        bicycle.Stops();


        car car = new car();
        car.start();
        car.wheels();
        car.Stops();

        bike bike = new bike();
        bike.start();
        bike.wheels();
        bike.Stops();

    }
}