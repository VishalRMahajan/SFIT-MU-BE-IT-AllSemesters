package userpackages;

public class user
{
    private String name;

    public user(String name)
    {
        this.name=name;
    }

    public void display()
    {
        System.out.print("Name of User is "+ name);
    }

}