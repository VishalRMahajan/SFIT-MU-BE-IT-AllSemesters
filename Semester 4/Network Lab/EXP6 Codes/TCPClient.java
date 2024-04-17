import java.io.*;
import java.net.*;

public class TCPClient {

  public static void main(String[] args) {
    try {
      // Connect to the server running on localhost at port 9999
      System.out.println("Connecting to the server...");
      Socket socket = new Socket("localhost", 9999);
      System.out.println("Connected to the server.");

      // Create input stream to read data sent by server
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(socket.getInputStream())
      );

      // Create output stream to send data to server
      PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

      // Send data to server
      System.out.println("Sending message to server...");
      writer.println("Hello from client!");

      // Read response from server and print
      System.out.println("Waiting for server response...");
      String serverResponse = reader.readLine();
      System.out.println("Server: " + serverResponse);

      // Close the streams and socket
      reader.close();
      writer.close();
      socket.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
