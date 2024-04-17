import java.io.*;
import java.net.*;

class Receivedata {
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(8888);
        byte[] b = new byte[1024];
        DatagramPacket dp = new DatagramPacket(b, 1024);
        ds.receive(dp);
        String s = new String(dp.getData(), 0, dp.getLength());
        System.out.println(s);
        ds.close();
    }
}
