import java.io.*;
import java.net.*;

public class TCPServer {

  public static void main(String[] args) {
    try {
      // Create a server socket listening on port 9999
      System.out.println("Server is waiting for client...");
      ServerSocket serverSocket = new ServerSocket(9999);
      System.out.println("Server socket created.");

      // Accept client connection
      System.out.println("Waiting for client to connect...");
      Socket clientSocket = serverSocket.accept();
      System.out.println("Client connected.");

      // Create input stream to read data sent by client
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(clientSocket.getInputStream())
      );

      // Create output stream to send data to client
      PrintWriter writer = new PrintWriter(
        clientSocket.getOutputStream(),
        true
      );

      // Read data from client and print
      System.out.println("Reading data from client...");
      String clientData = reader.readLine();
      System.out.println("Client: " + clientData);

      // Send response to client
      System.out.println("Sending response to client...");
      writer.println("Hello from server!");

      // Close the streams and sockets
      reader.close();
      writer.close();
      clientSocket.close();
      serverSocket.close();
      System.out.println("Server closed.");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
