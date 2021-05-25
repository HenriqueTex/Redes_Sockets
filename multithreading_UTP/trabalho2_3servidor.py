#Servidor TCP com Threads
#Henrique Teixeira Dumont e Kennedy Medeiros Soares
import socket
from _thread import *
import time 

HOST = 'localhost'              # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta
ThreadCount=0

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Parametros para IPV4 e protocolo TCP
s.bind((HOST,PORT))
print("Aguardando conexao")	
s.listen(5)

def client_thread(con):	
	
	while True:
		data=con.recv(2048)	#guardando a mensagem do cliente na variavel data
		hora=str.encode(time.strftime('%H:%M:%S', time.localtime()))	#criando uma variavel para receber a hore mo metodo time
		msg=str.encode("ola cliente, a hora do seu atendimento foi: ") # transformando a msg do servidor de uma string pra bytes
		if not data:			#fim da funcao quando nao houver mais mensagens
			break 
		con.sendall(msg+hora)		#devolvendo resposta do servidor ao cliente
		print(data.decode())
	con.close()				#fechando conexecao com o client

while True:
	
	cliente,end=s.accept()		#recebendo os dados do cliente conectado
	print("conectado a "+end[0]+str(end[1]))
	start_new_thread(client_thread,(cliente,))		#chamando a funcao cliente_thread em uma nova threand
	ThreadCount+=1
	print("Thread " +str(ThreadCount))			
	

s.close()
	
