import socket

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind((self.host,int(self.port)))
        #self.serverSocket.listen()
        print("<<< Socket created >>>")
        print("<<< Socket bind complete >>>")
    
    def start(self):
        while True:
            dataReceive, addressSocket = self.serverSocket.recvfrom(1024)
            print("Message [{}]: {}".format(addressSocket[0]+":"+str(addressSocket[1]), dataReceive.decode()))
            self.serverSocket.sendto(b'OK ::: ' + dataReceive, addressSocket)

if __name__ == '__main__':
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    HOST, PORT = ip_port.split()
    udpServer = UDPServer(HOST, PORT)
    udpServer.start()