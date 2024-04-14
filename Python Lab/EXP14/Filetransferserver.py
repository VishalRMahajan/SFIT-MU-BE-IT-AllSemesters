# File: FileTransferServer.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is started and listening for the client to connect")

    client_socket, addr = server_socket.accept()
    print(f"Client {addr} connected")

    with open('./Data/recievedfile.txt', 'wb') as file:
        print("File opened")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("File has been received successfully.")
    client_socket.close()

if __name__ == '__main__':
    start_server()