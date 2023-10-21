import random
import os
import sys

sys.path.append('stagios')
import batalha
sys.path.append('pokemons')
import pokemon_class
sys.path.append('player')
import pokemon_inventory
sys.path.append('sond')
import sond_control

Mus = sond_control.Mus()


def dialogo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
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
    print('')
    input('')


Mus.Mus_p("ost/welcome to pokemon/Welcome to the World of Pokémon! - Pokémon Ruby & Sapphire [High Quality] (320 kbps).mp3")


dialogo('olá Desculpe-me pela espera.')
dialogo('Bem... Seja bem vindo ao fabuloso mundo dos POKÉMONS!.')
dialogo('Eu me chamo carvalho.')
dialogo('Mas todo mundo aqui me chama de professor carvalho.')
dialogo('Aqui temos o que chamamos de pokémon.')
dialogo('Esse mundo é habitado por criaturas chamadas  de pokémons.')
dialogo('Os seres humanos e pokémons vivem em conjunto. As vezes,estamos bem')
dialogo('em conjunto. As vezes,estamos bem e ajudando uns aos outros.')
dialogo('As veses iremos nos unir e lutar contra outras equipes.')
dialogo('Mas, apesar desses vínculos, eu não sei muito sobre os pokémons.')
dialogo('Na verdade, existem muitos segredos em torno dos pokémons.')
dialogo('E na minha busca para descobrir, eu dediquei a minha vida à pesquisa.')
dialogo('Isso é o que eu faço atualmente.')
dialogo('E voçê é ?')


os.system('cls' if os.name == 'nt' else 'clear')
sexo = input("Um menino ou uma menina ? ")


while sexo != 'menino' and sexo != 'menina':
    os.system('cls' if os.name == 'nt' else 'clear')
    sexo = input("Um menino ou uma menina ? ")



os.system('cls' if os.name == 'nt' else 'clear')
nome = input("Certo. Como é o seu nome ? ")

dialogo('Ah, sim, agora eu lembro!')
dialogo('Voçê acaba de mudar para a minha cidade natal. Não é?')
dialogo('Ok, escute bem o que eu vou lhe dizer...')
dialogo('Sua própria aventura está começando agora.')
dialogo('Vá em frente e entre no mundo dos pokémons: um mundo de sonhos, cheio')
dialogo('de aventuras e grandes amigos.')
dialogo('Bem, venha me visitar logo. Vou esperar em meu laboratório pokémon')

dialogo('Ah, ola seja bem vindo ao meu laboratório.')
dialogo('Vamos, aproxime-se e escolha um dos pokemons dessa messa!')



#variavel do inventario do jogador
pkInvetory = pokemon_inventory.player_inventory()
iniInvetory = pokemon_inventory.inimigo_inventory()


os.system('cls' if os.name == 'nt' else 'clear')
escolha = input('Escolha um poskemon [1 - BULBASAUR],[2 - CHARMANDER],[3 - SQURTLE] ')


while escolha != '1' and escolha != '2' and escolha != '3':
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = input('Escolha um poskemon [1 - BULBASAUR],[2 - CHARMANDER],[3 - SQURTLE] ')

if escolha == '1':
    #o __class__ modifica a classe molde, tomar preucação quando fazer isso
    pkInvetory.__class__.pokemon_1 = pokemon_class.BULBASAUR()

if escolha == '2' :
    pkInvetory.__class__.pokemon_1 = pokemon_class.CHARMANDER()
    
if escolha == '3' :
    pkInvetory.__class__.pokemon_1 = pokemon_class.SQURTLE()
    


pkInvetory.__class__.pokemon_2 = pokemon_class.VOID()
pkInvetory.__class__.pokemon_3 = pokemon_class.VOID()
pkInvetory.__class__.pokemon_4 = pokemon_class.VOID()
pkInvetory.__class__.pokemon_5 = pokemon_class.VOID()
pkInvetory.__class__.pokemon_6 = pokemon_class.VOID()


dialogo('Serto, agora que voçê escolheu um pokemon porque voçê não tenta')
dialogo('batalhar contra o seu rival ?')




iniInvetory.__class__.pokemon_1 = pokemon_class.BULBASAUR()
iniInvetory.__class__.pokemon_2 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_3 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_4 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_5 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_6 = pokemon_class.VOID()


Mus.Stop()

batalha1 = batalha.combat()


