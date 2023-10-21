import sys



sys.path.append('stagios')
import batalha 
sys.path.append('pokemons')
import pokemon_class
sys.path.append('player')
import pokemon_inventory

#script de teste de batlhas

#acessa o inventario
pkInvetory = pokemon_inventory.player_inventory()

iniInvetory = pokemon_inventory.inimigo_inventory()

#cria um pokemon no inventario
pkInvetory.__class__.pokemon_1 = pokemon_class.BULBASAUR()
pkInvetory.__class__.pokemon_2 = pokemon_class.BULBASAUR()
pkInvetory.__class__.pokemon_3 = pokemon_class.BULBASAUR()
pkInvetory.__class__.pokemon_4 = pokemon_class.BULBASAUR()
pkInvetory.__class__.pokemon_5 = pokemon_class.BULBASAUR()
pkInvetory.__class__.pokemon_6 = pokemon_class.BULBASAUR()

pkInvetory.__class__.pokemon_2.NOME = 'Gasoso'
pkInvetory.__class__.pokemon_3.NOME = 'truta'
pkInvetory.__class__.pokemon_4.NOME = 'banana'
pkInvetory.__class__.pokemon_5.NOME = 'cachorro'
pkInvetory.__class__.pokemon_6.NOME = 'AAAAAAAA'



iniInvetory.__class__.pokemon_1 = pokemon_class.BULBASAUR()
iniInvetory.__class__.pokemon_2 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_3 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_4 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_5 = pokemon_class.VOID()
iniInvetory.__class__.pokemon_6 = pokemon_class.VOID()

iniInvetory.__class__.pokemon_1.XP = 20



#starta a batlha
batalha1 = batalha.combat()