import rsa

def cifrar_mensagem(msg):
    arqnomepub = "/home/ali/fatec-sjc/BDD/fateclando/andrePub.txt"
    ##abro o arquivo com a chave
    arq = open(arqnomepub,'rb')
    ##carrego a chave
    txt = arq.read()
    arq.close()
    #decodifico para o formato expoente e modulo
    pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')
    #cifro a msg
    msgc = rsa.encrypt(msg,pub)
    return msgc