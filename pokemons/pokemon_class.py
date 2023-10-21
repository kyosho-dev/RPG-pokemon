import random
import math


#nesse script fica a base dos pokemons
# normal, fogo,ferro,agua,eletrico, pedra, gelo, planta, psiquico

class pokemon:
        
    def random_atr(self):
        self.HP = random.randint(39,50)
        self.ATK = random.randint(40,70)
        self.DEF = random.randint(40,70)
        self.spATK = random.randint(40,70)
        self.spDEF = random.randint(40,70)
        self.SPEED = random.randint(40,70)
        
    def return_stat(self):
        print('\nHP = '+ str(self.HP))
        print('ATK = '+ str(self.ATK))
        print('spATK = '+ str(self.spATK))
        print('spDEF = '+ str(self.spDEF))
        print('SPEED = '+ str(self.SPEED))
        print('TIPO  = '+ str(self.TAIPE ))
        print('NOME = '+ str(self.NOME) + '\n')
    
    def check_xp(self,pk):
        if self.XP >= self.XP_prox:
            self.XP -= self.XP_prox
            self.LVL += 1
            self.XP_prox += 5


            pk.HP += random.randint(1,2)
            pk.ATK += random.randint(1,2)
            pk.DEF += random.randint(1,2)
            pk.spATK += random.randint(1,2)
            pk.spDEF += random.randint(1,2)
            pk.SPEED += random.randint(1,2)

            return True
    
    def check_hp(sel,pk):
        pass


class VOID(pokemon):
    
    def __init__(self):
        self.HP = 0
        self.HP_current = self.HP
        self.ATK = 0
        self.ATK_current = self.ATK
        self.DEF = 0
        self.DEF_current = self.DEF
        self.spATK = 0
        self.spATK_current = self.spATK
        self.spDEF = 0
        self.spDEF_current = self.spDEF
        self.SPEED = 0
        self.SPEED_current = self.SPEED

        self.TAIPE = ""  
        self.NOME = "Na"

        self.LVL = 0
        self.XP = 0
        self.XP_prox = 20

        self.atk_1_nome = "---"
        self.atk_1_usoMAX = 0
        self.atk_1_uso = 0

        self.atk_2_nome = "---"
        self.atk_2_usoMAX = 0
        self.atk_2_uso = 0

        self.atk_3_nome = "---"
        self.atk_3_usoMAX = 0
        self.atk_3_uso = 0

        self.atk_4_nome = "---"
        self.atk_4_usoMAX = 0
        self.atk_4_uso = 0
        

    golpes = {
    }


class BULBASAUR(pokemon):
    
    def __init__(self):
        self.HP = 45
        self.HP_current = self.HP
        self.ATK = 49
        self.ATK_current = self.ATK
        self.DEF = 49
        self.DEF_current = self.DEF
        self.spATK = 65
        self.spATK_current = self.spATK
        self.spDEF = 65
        self.spDEF_current = self.spDEF
        self.SPEED = 45
        self.SPEED_current = self.SPEED
        
        self.TAIPE = "PLANTA"  
        self.NOME = "BULBASAUR"

        self.LVL = 1
        self.XP = 0
        self.XP_prox = 20

        self.atk_1_nome = "Investida"
        self.atk_1_usoMAX = 35
        self.atk_1_uso = 35

        self.atk_2_nome = "---"
        self.atk_2_usoMAX = 0
        self.atk_2_uso = 0

        self.atk_3_nome = "---"
        self.atk_3_usoMAX = 0
        self.atk_3_uso = 0

        self.atk_4_nome = "---"
        self.atk_4_usoMAX = 0
        self.atk_4_uso = 0
        

    golpes = {
      
    }

    def userSkill(player, name, inimigo):
        f = eval(name)
        return f(player, inimigo)


class CHARMANDER(pokemon):
    
    def __init__(self):
        self.HP = 39
        self.HP_current = self.HP
        self.ATK = 52
        self.ATK_current = self.ATK
        self.DEF = 43
        self.DEF_current = self.DEF
        self.spATK = 60
        self.spATK_current = self.spATK
        self.spDEF = 50
        self.spDEF_current = self.spDEF
        self.SPEED = 65
        self.SPEED_current = self.SPEED

        self.TAIPE = "FOGO"  
        self.NOME = "CHARMANDER"

        self.LVL = 1
        self.XP = 0
        self.XP_prox = 20

        self.atk_1_nome = "Investida"
        self.atk_1_usoMAX = 35
        self.atk_1_uso = 35

        self.atk_2_nome = "---"
        self.atk_2_usoMAX = 0
        self.atk_2_uso = 0

        self.atk_3_nome = "---"
        self.atk_3_usoMAX = 0
        self.atk_3_uso = 0

        self.atk_4_nome = "---"
        self.atk_4_usoMAX = 0
        self.atk_4_uso = 0
        

    golpes = {
      
    }

    def userSkill(player, name, inimigo):
        f = eval(name)
        return f(player, inimigo)


class SQURTLE(pokemon):
    
    def __init__(self):
        self.HP = 44
        self.HP_current = self.HP
        self.ATK = 48
        self.ATK_current = self.ATK
        self.DEF = 65
        self.DEF_current = self.DEF
        self.spATK = 50
        self.spATK_current = self.spATK
        self.spDEF = 64
        self.spDEF_current = self.spDEF
        self.SPEED = 43
        self.SPEED_current = self.SPEED

        self.TAIPE = "ÁGUA"  
        self.NOME = "SQURTLE"

        self.LVL = 1
        self.XP = 0
        self.XP_prox = 20

        self.atk_1_nome = "Investida"
        self.atk_1_usoMAX = 35
        self.atk_1_uso = 35

        self.atk_2_nome = "---"
        self.atk_2_usoMAX = 0
        self.atk_2_uso = 0

        self.atk_3_nome = "---"
        self.atk_3_usoMAX = 0
        self.atk_3_uso = 0

        self.atk_4_nome = "---"
        self.atk_4_usoMAX = 0
        self.atk_4_uso = 0
        

    golpes = {
      
    }

    def userSkill(player, name, inimigo):
        f = eval(name)
        return f(player, inimigo)








golpes = {
      #[0,1,2,3,4,5,6] conjunto de dados de uma habilidade
      #nivel,nome,tipo,categoria     poder,precisão,uso
        1,'Investida','NORMAL','Físico',50,100,35,
        3, 'Rugido','NORMAL','Status',0,100,40,
        7, 'Semente sanguessuga','PLANTA','Status',0,90,10,
        9, 'Chicote de Vinha','PLANTA','Físico',35,100,15,
        13, 'Pó Venenoso','VENENO','Status',0,75,35

}



def danoFisico(player , inimigo, tipo, poder):

    LVLm = (int(player.LVL) + int(inimigo.LVL))/2
    

    if tipo == player.TAIPE:
        STAB = 1,5
    else:
        STAB = 1

    #Variaves para implementar no futuro

    WEAKNESSr = 1      # resistencia dos pokemons aos golpes
    CRITICAL = 1       # critico do golpe
    OTHERS = 1         # outos bonus

    #Marigin e a margem de erro que o ataque pode ter
    M = 100
    MARGIN = M/100

    #others é a variável para itens, habilidades, efeito de Burn,

    dano = math.floor (((((2*LVLm/5+2) * player.ATK_current * poder/inimigo.DEF_current) / 50) + 2) * STAB * WEAKNESSr * CRITICAL * OTHERS * MARGIN)

    return dano
    


def Investida(player , inimigo):
        LVLr = 1
        tipo = 'NORMAL'
        categoria ='Físico'
        poder = 50
        precisão = 100
        uso = 35


        
        damage = danoFisico(player,inimigo,tipo,poder)
        

        inimigo.HP_current = inimigo.HP_current - damage
        


        return 'batalha'

def Rugido(player , inimigo):
        #modificar para tirar apenas 6 pontos 
        LVLr = 3
        tipo = 'NORMAL'
        categoria ='Status'
        poder = 0
        precisão = 100
        uso = 40

        
        inimigo.ATK_current -= 1
        
        


        return 'batalha'

def SementeSanguessuga(player , inimigo):
        #que drena 1⁄8 de seu HP máximo no final de cada turno e
        #restaura para o usuário
        LVLr = 7
        tipo = 'PLANTA'
        categoria ='Status'
        poder = 0
        precisão = 90
        uso = 10


        
        damage = math.floor(inimigo.HP/8)
        

        inimigo.HP_current -= damage
        player.HP_current += damage
        


        return 'batalha'

def ChicoteDeVinha(player , inimigo):
        LVLr = 9
        tipo = 'PLANTA'
        categoria ='Físico'
        poder = 35
        precisão = 100
        uso = 15


        
        damage = danoFisico(player,inimigo,tipo,poder)
        

        inimigo.HP_current = inimigo.HP_current - damage
        


        return 'batalha'




    





