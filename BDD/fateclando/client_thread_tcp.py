#Cliente TCP
import socket
from threading import Thread
import rsa
from cifrar_mensagem import cifrar_mensagem
from decifrar_mensagem import decifrar_mensagem


global tcp_con

def receber():
    global tcp_con
    while True:
        msgc = tcp_con.recv(1024)
        if not msgc: break
        msg = decifrar_mensagem(msgc)
        print ("Server:",msg)

def enviar():
    global tcp_con
    print ('Para sair use CTRL+X\n')
    msg = input().encode('utf-8')
    msgc = cifrar_mensagem(msg)
    while msg != '\x18':
        tcp_con.send(msgc)
        msg = input().encode('utf-8')
        msgc = cifrar_mensagem(msg)
    tcp_con.close()

# Endereco IP do Servidor
SERVER = '10.212.134.105'

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
