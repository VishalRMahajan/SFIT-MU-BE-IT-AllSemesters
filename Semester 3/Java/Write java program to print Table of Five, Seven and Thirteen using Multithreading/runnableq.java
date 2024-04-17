class Five implements Runnable {

    public void run() {

        for(int i=1;i<11;i++)
        {   
            int j=5*i;
            System.out.println("5 X "+ i + "= "+j);
        }

    }

}

class Seven implements Runnable {
    public void run() {
        for(int i=1;i<11;i++)
        {   
            int j=7*i;
            System.out.println("7 X "+ i + "= "+j);
        }
    }
}

class Thirteen implements Runnable {
    public void run() {
        for(int i=1;i<11;i++)
        {   
            int j=13*i;
            System.out.println("13 X "+ i + "= "+j);
        }
    }
}

public class runnableq {
    public static void main(String[] args) {
        Five five = new Five();
        Seven seven = new Seven();
        Thirteen thirteen = new Thirteen();

        Thread T1 = new Thread(five);
        Thread T2 = new Thread(seven);
        Thread T3 = new Thread(thirteen);

        T1.run();
        T2.run();
        T3.run();

    }
}