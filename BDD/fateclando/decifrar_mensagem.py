import rsa

def decifrar_mensagem(msgc):
        arqnomepri = "/home/ali/fatec/FATEC/Banco de dados Distribuídos/atividade_7/fateclando/criptografiachavePri.txt"
        ##abro o arquivo com a chave
        arq = open(arqnomepri,'rb')
        ##carrego a chave
        txt = arq.read()
        arq.close()

        #decodifico para o formato expoente e modulo
        pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')    

        #decifro a msg
        msg = rsa.decrypt(msgc,pri)
        return msg