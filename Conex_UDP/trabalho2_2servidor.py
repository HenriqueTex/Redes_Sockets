#Servidor UDP
#Henrique Teixeira Dumont e Kennedy Medeiros Soares
import socket
import time

HOST = 'localhost'              # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Parametros para IPV4 e protocolo UDP

s.bind((HOST,PORT))	
print("aguardando conexao")


while True:
	data,end= s.recvfrom(1024)		#armazenando a mensagem recebida e o endereco do cliente
	msg =str.encode("ola cliente, obrigado por sua mensagem. Minha hora e: ")
	hora=str.encode(time.strftime('%H:%M:%S', time.localtime())) #criando uma variavel para receber a hore mo metodo time
	s.sendto(msg+hora,end)			#enviando mensagem e hora para utilizando o endereco do cliente
	print(data.decode())

