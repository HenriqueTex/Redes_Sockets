#Servidor TCP
#Henrique Teixeira Dumont e Kennedy Medeiros Soares
import socket
import time


HOST= 'localhost'    #estabelecendo o endereco de ip como a maquina local	
PORT= 50000	      #definindo a porta que sera utilizada pelo servidor

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Parametros para IPV4 e protocolo TCP
s.bind((HOST,PORT))	
s.listen(1)

print("Aguardando conexao do cliente")

con,end =s.accept()  #variaveis de conexao e endereco recebendo metodo que aceita a conexao

print("Conectado em ", end)

msg=str.encode("ola cliente, obrigado pela mensagem. Minha hora e: ")


while True:

    data=con.recv(1024)  #Armazenando o que foi recebido do cliente na variavel data
    
    
    if not data:        
        con.close()	#finalizando a conexecao quando nao tiver mais dados a serem recebidos
        break

    hora=str.encode(time.strftime('%H:%M:%S', time.localtime()))	#criando uma variavel para receber a hore mo metodo time
    con.send(msg + hora)
    
    print(data.decode())
    
