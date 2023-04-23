import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.host,int(self.port)))
    
    #def send_message(self):
        

    def start(self):
        print("Connected to", self.host, "on port", self.port)
        print("To end the program, type 'close'")
        message = ""
        cont = 0
        while message.lower() != "close": 
            message = input("Message to send...: ")
            self.clientSocket.sendall(message.encode())
            data = self.clientSocket.recv(1024)
            print(f"Server reply......: [{cont}]", data.decode())
            cont += 1

if __name__ == '__main__':
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    #PORT = input("Port [Default: 8080]: ") or 8080
    HOST, PORT = ip_port.split()
    tcpClient = TCPClient(HOST,PORT)
    tcpClient.start()