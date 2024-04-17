public class sleepthread
{
    public static void main(String[] args) {
        try{    
                System.out.println("Main thread is slepping...");
                Thread.sleep(500);
                System.out.println("main thread woke up!");
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}