//Create two threads such that one thread will print even number and another will print odd number in  an ordered fashion

class even extends Thread
{
   public void run()
   {    
     System.out.println("Even Numbers : \n");
        for(int i=0;i<=10;i+=2)
        {
            System.out.println(i);
        }
   }
}

class odd extends Thread
{
    public void run()
    {
         System.out.println("ODD Numbers : \n");
        for(int i=1;i<=10;i+=2)
        {
            System.out.println(i);
        }
    }
}

public class evenodd
{
    public static void main(String[] args) {
        even even= new even();
        odd odd = new odd();
        even.start();
        odd.start();
    }
}