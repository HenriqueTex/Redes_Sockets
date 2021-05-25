#Servidor UDP com trheads
#Henrique Teixeira Dumont e Kennedy Medeiros Soares
import socket
from _thread import *
import time 

HOST = 'localhost'              # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta
ThreadCount=0

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#Parametros para IPV4 e protocolo TCP
s.bind((HOST,PORT))
print("Aguardando conexao")	


def client_thread(end,data):	
			
	hora=str.encode(time.strftime('%H:%M:%S', time.localtime()))	#criando uma variavel para receber a hore mo metodo time
	msg=str.encode("ola cliente, a hora do seu atendimento foi: ") # transformando a msg do servidor de uma string pra bytes
	s.sendto(msg+hora,end)	
	print(data.decode())
					

while True:
	
	data,end= s.recvfrom(2048)		#recebendo endereco e mensagem do cliente	
	start_new_thread(client_thread,(end,data))		#chamando a funcao cliente_thread em uma nova threand
	ThreadCount+=1
	print("Thread " +str(ThreadCount))			
	

s.close()
	
