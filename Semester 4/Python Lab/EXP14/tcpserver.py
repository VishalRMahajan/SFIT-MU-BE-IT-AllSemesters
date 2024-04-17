import socket
if __name__=="__main__":
    ip = "127.0.0.1"
    port = 3600
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.bind((ip ,port))
    server.listen(5)
    print("SSP is Ready to Receive the Request from CSP")
    while True:
        clientsoc, caddr=server.accept()
        csdata=clientsoc.recv(1024)
        csdata=csdata.decode("utf-8")
        print("Student Msg-->{}".format(csdata))
        ssdata=input("Teacher Msg-->")
        clientsoc.send(ssdata.encode())