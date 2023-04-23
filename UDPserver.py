#Importa do modulo socket
import socket

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        #Cria o socket UDP
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        #Conecta o socket ao host e porta especificados
        self.serverSocket.bind((self.host,int(self.port)))

        #Exibe mensagem informando que o socket foi criado e associado com sucesso
        print("<<< Socket created >>>")
        print("<<< Socket bind complete >>>")
    
    def start(self):
        while True:
            #Aguarda a chegada de dados
            dataReceive, addressSocket = self.serverSocket.recvfrom(1024)

            #Exibe o endereço do cliente e a mensagem recebida
            print("Message [{}]: {}".format(addressSocket[0]+":"+str(addressSocket[1]), dataReceive.decode()))

            #Envia uma resposta para o cliente
            self.serverSocket.sendto(b'OK ::: ' + dataReceive, addressSocket)

if __name__ == '__main__':
    #Pede ao usuario o endereço IP e a porta
    ip_port = input("Host/IP Port [Default: localhost 8080]: ") or 'localhost 8080'
    HOST, PORT = ip_port.split()

    #Instancia o objeto UDPServer e inicia a conexao
    udpServer = UDPServer(HOST, PORT)
    udpServer.start()