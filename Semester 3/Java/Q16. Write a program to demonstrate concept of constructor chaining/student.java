class student {
    private  int pid;
    private  String name;
    private  String Department;

    public student(int pid) {
        this.pid = pid;
        System.out.println("Pid of Student is " + pid);
    }

    public student(int pid, String name) {
        this(pid);
        this.name = name;
        System.out.println("Name of Student is " + name);
    }

    public student(int pid, String name, String Department) {
        this(pid,name);
        this.Department=Department;
        System.out.println("Department of Student is " + Department);
    }

    public static void main(String[] args)
    {
        student Studnet = new student(221068,"Vishal","IT");
    }
}