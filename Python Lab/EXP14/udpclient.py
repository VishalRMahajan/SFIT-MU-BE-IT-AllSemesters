import socket

if __name__=="__main__":
    ip = "127.0.0.1"
    port = 3600
    while True:
        client = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        csdata=input("Student Msg-->")
        client.sendto(csdata.encode(), (ip, port))
        ssdata, addr = client.recvfrom(1024)
        print("Teacher Msg-->{}".format(ssdata.decode()))