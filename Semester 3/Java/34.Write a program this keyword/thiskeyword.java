class thiskeyword
{
    private String name;

    public thiskeyword(String name)
    {
        this.name=name;
    }

    public void display(){
        System.out.println("Name of Person is "+ this.name);
    }

    public static void main(String[] args) {
        thiskeyword thiskeyword = new thiskeyword("Vishal");
        thiskeyword.display();
    }
}