import socket

if __name__=="__main__":
    ip = "127.0.0.1"
    port = 3600
    while True:
        client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client.connect((ip , port))
        csdata=input("Student Msg-->")
        client.send(csdata.encode())
        ssdata=client.recv(1024).decode()
        print("Teacher Msg-->{}".format(ssdata))