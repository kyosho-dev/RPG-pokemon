import socket
import threading
import time
import json

import sys
#importa as coisas do jogo
sys.path.append('stagios')
import batalha 
sys.path.append('pokemons')
import pokemon_class
sys.path.append('player')
import pokemon_inventory

# Configurações do servidor
host = '127.0.0.1'
port = 12345

#comandos do servidor
cm1 = '-c' #mostra os sockets conectados
cm2 = '-p' #mostra os player conectados com os respectivos sokets
cm3 = ''


Players = []
Players_name = [] #0-sokt do jogador-1 nome do jogador
mensagens = []

room1 = []
room2 = []
room3 = []
room4 = []


Server_info = {
        'nRoom1': 0,
        'Room1Starter': False,
        'nRoom2': 0,
        'Room2Starter': False,
        'nRoom3': 0,
        'Room3Starter': False,
        'nRoom4': 0,
        'Room4Starter': False,
        'context': "", #comando ou contexto do cliente
}



# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Liga o socket ao endereço e porta desejados
server_socket.bind((host, port))
# Coloca o socket em modo de escuta
server_socket.listen()


#escuta e execulta o que o clinte quer fazer
def handle_client(client_socket, client_address):
    register = False

    print(f"Conexão estabelecida com {client_address}")
    
    while True:
        try:
            #data é o que o cliente envia para o server 
            data = client_socket.recv(1024).decode('utf-8')
            received_data = json.loads(data)

            
            #atrela o sockt com o nome do jogador
            
            if received_data['username'] != '' and register == False:
                Players_name.append(client_socket)
                Players_name.append(received_data['username'])
                register = True


            if received_data['context'] == 'NumberUserRoom':
                Server_info['nRoom1'] = len(room1)/2
                Server_info['nRoom2'] = len(room2)/2
                Server_info['nRoom3'] = len(room3)/2
                Server_info['nRoom4'] = len(room4)/2

                ServerInvite_data = json.dumps(Server_info)
                client_socket.send(ServerInvite_data.encode('utf-8'))
            
            if received_data['context'] == 'UserEnterRoom1' and len(room1) < 4:
                if not(client_socket in room1):
                    room1.append(client_socket)
                    room1.append(received_data['username'])
            
            
            # inicia o jogo
            if received_data['context'] == 'StartRoom1' and len(room1) == 4:
                print('sala 1 iniciou o jogo')
                if not(client_socket in room1):
                    room1.append(client_socket)
                    room1.append(received_data['username'])


                
            if not data:
                break

            print(f"Cliente {client_address}: {received_data['message']}")
            mensagens.append(data)
            mensagenP_todos(client_socket, data)

            
            

        except ConnectionResetError:
            Players.remove(client_socket)
            Players_name.remove(client_socket)
            Players_name.remove(received_data['username'])
            print(f"Conexão com {client_address} foi forçada a ser fechada pelo cliente.")
            break
            

    #client_socket.close()
    #print(f"Conexão com {client_address} encerrada")

#fica de fundo aguardando novas conexões é cria um novo processo 
def aguardando_client():
    while True:
        # Aceita uma conexão quando ela é feita. a função do serve fica escutando
        # emquanto não entrar um cliente o servidor não execulta a linha de baixo
        client_socket, client_address = server_socket.accept()
        Players.append(client_socket)
        
        

        # cria uma thread que funciona  a parte do codico principal execultando uma função
        #client_socket usa para conversar com aquele cliente
        #client_address e apena as informações da porta é do ip do cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

#controle de mensagens do chat
def mensagenP_todos(client_socket,data):
    for i in Players:
        if i != client_socket:
            print(i)
            i.send(data.encode('utf-8'))


#funções de comando do terminal do servidor
def controle_comandos():
    while True:
        comands = input('')

        if comands == cm1:
            mostar_clients()

        if comands == cm2:
            mostar_players()

def mostar_clients():
    print(f'Lista de Clientes conectados:{Players}')

def mostar_players():
    print(f'Lista de players conectados:{Players_name}')



print(f"Iniciando o server...")
print(f"Aguardando conexões em {host}:{port}...")


client_thread = threading.Thread(target=aguardando_client)
client_thread.start()

client_thread = threading.Thread(target=controle_comandos)
client_thread.start()




