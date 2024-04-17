import java.io.*;
import java.net.*;

class Senddata {
    public static void main(String[] args) throws IOException {
        DatagramSocket ds = new DatagramSocket();
        String s = "";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();
        InetAddress ip = InetAddress.getByName("localhost");
        DatagramPacket dp = new DatagramPacket(s.getBytes(), s.length(), ip, 8888);
        ds.send(dp);
        ds.close();
    }
}
