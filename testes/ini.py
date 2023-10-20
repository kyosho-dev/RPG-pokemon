<<<<<<< HEAD
import os
import time
import sys

#140 caracteres

def intro():

        os.system('cls' if os.name == 'nt' else 'clear')
        largura = 1
        caractere = "\u2588"
        cor = "\033[97m"

        colchetes = (cor + caractere) * largura + "\033[0m"
        delay = 0.000005

        
        for i in range(1,2364):
            print(colchetes, end='')
            sys.stdout.flush()
            time.sleep(delay)

        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

        time.sleep(0.1)

        

        for i in range(1,2364):
            print(colchetes, end='')
            sys.stdout.flush()
        
        time.sleep(0.1)

        os.system('cls' if os.name == 'nt' else 'clear')
        
        



intro()










=======
import os
import time
import sys

#140 caracteres

def intro():

        os.system('cls' if os.name == 'nt' else 'clear')
        largura = 1
        caractere = "\u2588"
        cor = "\033[97m"

        colchetes = (cor + caractere) * largura + "\033[0m"
        delay = 0.000005

        
        for i in range(1,2364):
            print(colchetes, end='')
            sys.stdout.flush()
            time.sleep(delay)

        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

        time.sleep(0.1)

        

        for i in range(1,2364):
            print(colchetes, end='')
            sys.stdout.flush()
        
        time.sleep(0.1)

        os.system('cls' if os.name == 'nt' else 'clear')
        
        



intro()










>>>>>>> da22c5d3b9fdadea95ca37c6fb899ba889e6a480
