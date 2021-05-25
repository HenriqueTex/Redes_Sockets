#Cliente TCP
#Henrique Teixeira Dumont e Kennedy Medeiros Soares
import socket
import time


HOST= 'localhost'   #estabelecendo o endereco de ip como a maquina local
PORT= 50000	  ##definindo a porta que sera utilizada pelo servidor

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Parametros para IPV4 e protocolo TCP
s.connect((HOST,PORT))

hora=str.encode(time.strftime('%H:%M:%S', time.localtime())) #criando uma variavel para receber a hore mo metodo time
msg=str.encode("Oi servidor,eu sou o cliente 03 minha hora e:")
s.send(msg+hora)


data=s.recv(1024) #armazenando dados devolvidos do servidor para a variavel data

print(data.decode())


