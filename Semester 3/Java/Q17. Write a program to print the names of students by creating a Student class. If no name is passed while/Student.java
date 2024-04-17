/*17. Write a program to print the names of students by creating a Student class. If no name is passed while 
creating an object of Student class, then the name should be Unknown, otherwise the name should be 
equal to the String value passed while creating object of Student class (use constructor concept) */


class Student
{
    private String Student1;
    private String Student2;

    public Student()
    {
         System.out.println("Passed without Parameter");
        this.Student1="Unkonwn";
        this.Student2="Unkonwn";

        System.out.println("Name of Studnet 1 is "+ Student1);
        System.out.println("Name of Studnet 2 is "+ Student2);
        System.out.println("\n");
        
    }

    public Student(String Student1, String Student2)
    {    
        System.out.println("Passed with Parameter");
        this.Student1=Student1;
        this.Student2=Student2;

        System.out.println("Name of Studnet 1 is "+ Student1);
        System.out.println("Name of Studnet 2 is "+ Student2);
    }


    public static void main(String[] args) {
        Student object1= new Student();
        Student pbject2= new Student("Vishal","Shubham");
    }
}