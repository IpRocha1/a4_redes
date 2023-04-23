#Importa do modulo socket
import socket

class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        #Criacao do socket TCP
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Conecta o socket ao host e porta especificados
        self.serverSocket.bind((self.host,int(self.port)))

        #Habilita o socket para receber conexoes
        self.serverSocket.listen()

        #Mensagem para indicar que o socket foi criado e associado a um endereço e porta
        print("<<< Socket created >>>")
        print("<<< Socket bind complete >>>")
    
    def start(self):

        #Aceita uma nova conexao e cria um novo socket para comunicacao com o cliente
        connectionSocket, addressSocket = self.serverSocket.accept()
        with connectionSocket:

            #Mensagem para indicar que houve a conexao
            print('Connected by', addressSocket)

            while True:
                #Recebe uma mensagem do cliente
                data = connectionSocket.recv(1024)

                #Imprime a mensagem recebida e o endereço do cliente que a enviou
                print("Message [{}]: {}".format(addressSocket[0]+":"+str(addressSocket[1]), data.decode()))

                #Envia uma resposta ao cliente
                connectionSocket.sendall(b'OK ::: ' + data)

if __name__ == '__main__':
    #Pede ao usuario o endereço IP e a porta
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    HOST, PORT = ip_port.split()

    #Instancia o objeto TCPServer e inicia a conexao
    tcpServer = TCPServer(HOST, PORT)
    tcpServer.start()