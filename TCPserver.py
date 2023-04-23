import socket

class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.host,int(self.port)))
        self.serverSocket.listen()
        print("<<< Socket created >>>")
        print("<<< Socket bind complete >>>")
    
    def start(self):
        connectionSocket, addressSocket = self.serverSocket.accept()
        with connectionSocket:
            print('Connected by', addressSocket)
            while True:
                data = connectionSocket.recv(1024)
                if not data:
                    break
                print("Message [{}]: {}".format(addressSocket[0]+":"+str(addressSocket[1]), data.decode()))
                connectionSocket.sendall(b'OK ::: ' + data)

if __name__ == '__main__':
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    #PORT = input("Port [Default: 8080]: ") or 8080
    HOST, PORT = ip_port.split()
    tcpServer = TCPServer(HOST, PORT)
    tcpServer.start()