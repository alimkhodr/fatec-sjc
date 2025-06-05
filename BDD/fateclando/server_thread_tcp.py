#Servidor TCP
import socket
from threading import Thread
from cifrar_mensagem import cifrar_mensagem
from decifrar_mensagem import decifrar_mensagem

global tcp_con

def enviar():
    global tcp_con
    msg = input().encode('utf-8')
    msgc = cifrar_mensagem(msg)
    while True:
        tcp_con.send(msgc)
        msg = input().encode('utf-8')
        msgc = cifrar_mensagem(msg)

# Endereco IP do Servidor
HOST = ''

# Porta que o Servidor vai escutar
PORT = 5004

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msgc = tcp_con.recv(1024)
        if not msgc: break
        #decifro a msg
        msg = decifrar_mensagem(msgc)

        print("Cliente:",msg)
    print ('Finalizando conexao do cliente', cliente)
    tcp_con.close()
