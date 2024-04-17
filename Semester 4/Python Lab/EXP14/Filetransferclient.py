# File: FileTransferClient.py
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to the server...")

    with open('.\Data\sendingfile.txt', 'rb') as file:
        print("Sending file...")
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    print("File has been sent successfully.")
    client_socket.close()

if __name__ == '__main__':
    start_client()