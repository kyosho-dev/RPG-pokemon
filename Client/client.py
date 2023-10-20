import threading
import sys
import os

import socket
import json

import queue
from colorama import Fore, Back, Style, init


# Configurações do cliente
#qual e o host é a porta do servidor 
host = '127.0.0.1'
port = 12345

# Cria um socket TCP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket ao servidor
servidor_socket.connect((host, port))
print(f"Conectado ao servidor em {host}:{port}")


print_lock = threading.Lock()  # Cria um lock para controlar a impressão no console
received_messages_queue = queue.Queue()
init(autoreset=True)  # Inicializa o colorama para automático de reset de formatação


userName = ''
section = 'Principal'
Principal = 'Principal'

user_info = {
        'username': userName,
        'message': "",
        'password': "",
        'Email': "",
        'context': "", #comando ou contexto do cliente
}

received_data = {}

# Recebe a resposta do servidor
def Dados_server():
    global received_data
    while True:
        # fica esperando ate receber a mensagem 
        data = servidor_socket.recv(1024).decode('utf-8')
        received_data = json.loads(data)
        received_messages_queue.put(received_data)


        #processar o que fazer com os dados
        
#limpa o chat e coloca o texto em cima
def print_received_messages():
    while True:
        if section == 'Chat':
            if not received_messages_queue.empty():
                message = received_messages_queue.get()

                # Limpa a linha e imprime a mensagem recebida
                with print_lock:
                    sys.stdout.write(Fore.RED + "\r" +message['username']+ ":"  + message['message']+'             ')
                    print("\n" + userName + ": ", end="")  # Mantém o prompt na mesma linha

def Send_data():
    serialized_data = json.dumps(user_info).encode('utf-8')

    servidor_socket.send(serialized_data)

















#telas que serão mostradas

def MenuPrincipal():

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Login ()')
    print('Cadastro ()' )
    print('Informações ()')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    section = input('')

    #filtro do que pode digitar

    if section != 'Login' and section != 'Cadastro' and section != 'Informações':
        section = Principal
    
    return section



def Login():

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Digite o seu nome: ')
    print('Cadastro ()' )
    print('Informações ()')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    section = input('')

    #filtro do que pode digitar

    if section != 'Login' and section != 'Cadastro' and section != 'Informações':
        section = Principal
    
    return section

def Cadastro():
    global userName

    os.system('cls' if os.name == 'nt' else 'clear')
    name = input('Digite o seu nome: ')
    password = input('Digite a sua senha: ' )
    Email = input('Digite o seu Email: ')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    userName = name
    user_info['username'] = name
    section = 'Menu1'
    Send_data()
    
    return section



def Menu1():

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Chat ()')
    print('Jogar ()' )
    print('Informações ()')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    section = input('')

    #filtro do que pode digitar

    if section != 'Chat' and section != 'Jogar' and section != 'Informações':
        section = 'Menu1'
    

    if section == 'Chat':
        os.system('cls' if os.name == 'nt' else 'clear')

        
    return section


def Jogar():

    user_info['context'] = 'NumberUserRoom'
    Send_data()
    user_info['context'] = ''

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sala 1 2/'+ str(received_data['nRoom1']))
    print('Sala 2 2/'+ str(received_data['nRoom2']))
    print('Sala 3 2/'+ str(received_data['nRoom3']))
    print('Sala 4 2/'+ str(received_data['nRoom4']))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Voltar')
    section = input('')

    

    #filtro do que pode digitar

    if section != 'Sala 1' and section != 'Sala 2' and section != 'Sala 3' and section != 'Sala 4' and section != 'Voltar':
        section = 'Jogar'
    

    if section == 'Sala 1':
        user_info['context'] = 'UserEnterRoom1'
        Send_data()
        user_info['context'] = ''
        section = 'Sala'

      
    return section


def Sala():

    user_info['context'] = 'NumberUserRoom'
    Send_data()
    user_info['context'] = ''

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sala 1 2/'+ str(received_data['nRoom1']))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Voltar')
    section = input('')

    

    #filtro do que pode digitar

    if section != 'Start' and section != 'Voltar':
        section = 'Sala'
    

    if section == 'Start':
        user_info['context'] = 'StartRoom1'
        Send_data()
        user_info['context'] = ''

        
    return section


def Chat():
    # Envia uma mensagem para o servidor
    user_info['message'] = input(userName + ": ")
    user_info['context'] = 'chat'
    Send_data()
    user_info['message'] = ''
    user_info['context'] = ''


    return 'Chat'


    

#recebe os dados do server
client_thread = threading.Thread(target=Dados_server)
client_thread.start()


while True:

    if section == Principal:
        section = MenuPrincipal()
    if section == 'Login':
        section = Login()
    
    if section == 'Cadastro':
        section = Cadastro()
    


    if section == 'Menu1':
        section = Menu1()
    if section == 'Chat':
        #conserta o chat
        print_thread = threading.Thread(target=print_received_messages)
        print_thread.start()
        section = Chat()
    if section == 'Jogar':
        section = Jogar()
    if section == 'Sala':
        section = Sala()
    

print('saiu')
    

    

# Fecha o socket
servidor_socket.close()
