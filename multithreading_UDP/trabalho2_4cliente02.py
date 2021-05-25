#Cliente UDP
#Henrique Teixeira Dumont e Kennedy Medeiros Soares

import socket
import time

HOST = 'localhost'              # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hora=str.encode(time.strftime('%H:%M:%S', time.localtime())) #criando uma variavel para receber a hore mo metodo time
msg=str.encode("Ola servidor, sou o cliente 02, minha hora e: ")
s.sendto((msg + hora),(HOST,PORT))

data,end=s.recvfrom(1024)
print(data.decode())

s.close()

