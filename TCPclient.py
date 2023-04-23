#Importa do modulo socket
import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        #Cria o socket TCP
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Conecta o socket ao host e porta especificados
        self.clientSocket.connect((self.host,int(self.port)))        

    def start(self):
        #Apresenta em tela o host e a porta que esta conectada
        print("Connected to", self.host, "on port", self.port)
        print("To end the program, type 'close'")
        message = ""
        cont = 0

        #Le a mensagem do usuario
        #Para fechar o socket pode digitar a palavra 'close'
        while message.lower() != "close": 
            message = input("Message to send...: ")
            self.clientSocket.sendall(message.encode())
            data = self.clientSocket.recv(1024)
            print(f"Server reply......: [{cont}]", data.decode())
            cont += 1

if __name__ == '__main__':
    #Pede ao usuario o endereço IP e porta do servidor
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    HOST, PORT = ip_port.split()

    #Instancia o objeto TCPClient e inicia a conexao
    tcpClient = TCPClient(HOST,PORT)
    tcpClient.start()