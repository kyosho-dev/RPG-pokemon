import os
import sys
import random
import time

sys.path.append('sond')
import sond_control
Mus = sond_control.Mus()








#tudo o que acontesse em uma batalha esta aqui dentro
class combat():


    spc1 = ' ' * 114
    spc2 = ' ' * 110
    spc3 = ' ' * 119
    spc4 = ' ' * 81
    spc5 = ' ' * 99
    spc6 = ' ' * 119
    spc7 = ' ' * 105
    spc8 = ' ' * 112
    spc9 = ' ' * 101
    spc10 = ' ' * 112
    spc11 = ' ' * 106
    spc12 = ' ' * 101

    inbatalhe = True
    section = 'batalha'
    escapar = 0
    podeEscapar = False

    turno = 'player'

    #NOME de comandos de acesso a menus


    Lutar = 'L'
    Mochila = 'M'
    Pokemon = 'P'
    Correr = 'C'
    Voltar = 'V'


    at1 = 'AT1'
    at2 = 'AT2'
    at3 = 'AT3'
    at4 = 'AT4'


    pk2 = 'PK2'
    pk3 = 'PK3'
    pk4 = 'PK4'
    pk5 = 'PK5'
    pk6 = 'PK6'
        

    

 

    def initBatalha(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
        print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('' + self.spc3 + self.pokemon_1.NOME +'    Lvl ' + str(self.pokemon_1.LVL))
        print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
        print('')
        print('o que' + self.spc1 + 'LUTAR'+ '    ' + 'MOCHILA')
        print('voçê faz?' + self.spc2 + 'POKEMON' + '  ' + 'CORRER')
        print('')
        section = input('')

        #filtro do que pode digitar
        if section != self.Lutar and section != self.Mochila and section != self.Pokemon and section != self.Correr:
            section = 'batalha'

        return section
        
    def LUTAR(self):

        

        #corrige a posição do texto
        value = 10 - len(self.pokemon_1.atk_1_nome)
        spcD1 = ' ' * value

        value = 10 - len(self.pokemon_1.atk_2_nome)
        spcD2 = ' ' * value

        value = 10 - len(self.pokemon_1.atk_3_nome)
        spcD3 = ' ' * value

        value = 10 - len(self.pokemon_1.atk_4_nome)
        spcD4 = ' ' * value



        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
        print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('' + self.spc3 + self.pokemon_1.NOME +'    Lvl ' + str(self.pokemon_1.LVL))
        print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
        print('')
        print(self.pokemon_1.atk_1_nome + spcD1 + 'PP ' + str(self.pokemon_1.atk_1_uso) + '/' + str(self.pokemon_1.atk_1_usoMAX) + '    ' + self.pokemon_1.atk_3_nome + spcD3 + 'PP ' + str(self.pokemon_1.atk_3_uso) + '/' + str(self.pokemon_1.atk_3_usoMAX) + self.spc4 + 'VOLTAR')
        print(self.pokemon_1.atk_2_nome + spcD2 + 'PP ' + str(self.pokemon_1.atk_2_uso) + '/' + str(self.pokemon_1.atk_2_usoMAX) + '    ' + self.pokemon_1.atk_4_nome + spcD4 + 'PP '  + str(self.pokemon_1.atk_4_uso) + '/' + str(self.pokemon_1.atk_4_usoMAX))
        print('')
        section = input('')

        #filtro do que pode digitar

        
        


        

        if section != self.Voltar and section != self.at1 and section != self.at2 and section != self.at3 and section != self.at4:
            section = self.Lutar


        if section == self.Voltar:
            section = 'batalha'


        ataque_1 = self.pokemon_1.atk_1_nome
        ataque_2 = self.pokemon_1.atk_2_nome
        ataque_3 = self.pokemon_1.atk_3_nome
        ataque_4 = self.pokemon_1.atk_4_nome




        if section == self.at1:
            if self.pokemon_1.atk_1_uso > 0:
                self.pokemon_1.atk_1_uso = self.pokemon_1.atk_1_uso - 1
                self.text((self.pokemon_1.NOME + ' usou'),ataque_1)
                section = self.pokemon_1.userSkill(ataque_1, self.IN_pokemon_1)

                self.exTurno()
            else:
                section = 'batalha'

        if section == self.at2:
            if self.pokemon_1.atk_2_uso > 0:
                self.pokemon_1.atk_2_uso = self.pokemon_1.atk_2_uso - 1
                self.text((self.pokemon_1.NOME + ' usou'),ataque_2)
                section = self.pokemon_1.userSkill(ataque_2, self.IN_pokemon_1)

                self.exTurno()
            else:
                section = 'batalha'
        
        if section == self.at3:
            if self.pokemon_1.atk_3_uso > 0:
                self.pokemon_1.atk_3_uso = self.pokemon_1.atk_3_uso - 1
                self.text((self.pokemon_1.NOME + ' usou'),ataque_3)
                section = self.pokemon_1.userSkill(ataque_3, self.IN_pokemon_1)

                self.exTurno()
            else:
                section = 'batalha'
        
        if section == self.at4:
            if self.pokemon_1.atk_4_uso > 0:
                self.pokemon_1.atk_4_uso = self.pokemon_1.atk_4_uso - 1
                self.text((self.pokemon_1.NOME + 'usou'),ataque_4)
                section = self.pokemon_1.userSkill(ataque_4, self.IN_pokemon_1)

                self.exTurno()
            else:
                section = 'batalha'

       
        
        
            




        return section

    def MOCHILA(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.item_1+'        '+ self.item_11)
        print(self.item_2+'        '+ self.item_12)
        print(self.item_3+'        '+ self.item_13)
        print(self.item_4+'        '+ self.item_14)
        print(self.item_5+'        '+ self.item_15)
        print(self.item_6+'        '+ self.item_16)
        print(self.item_7+'        '+ self.item_17)
        print(self.item_8+'        '+ self.item_18)
        print(self.item_9+'        '+ self.item_19)
        print(self.item_10+'        '+ self.item_20)
        print('')
        print(''+ self.spc6 + 'VOLTAR')
        print('escolha um item'+ self.spc5)
        print('')
        section = input('')

        #filtro do que pode digitar
        if section != self.Voltar and section != 'ataque 1' and section != 'ataque 2' and section != 'ataque 3' and section != 'ataque 4':
            section = self.Mochila
        if section == self.Voltar:
            section = 'batalha'
        return section

    def POKEMON(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        for i in range(1,7):
            pokemon_var = getattr(self, f"pokemon_{i}")

            if pokemon_var.NOME == 'Na':
                print('Na')
            else:
                print(pokemon_var.NOME + '    Lvl ' + str(pokemon_var.LVL) + '    HP ' + str(pokemon_var.HP_current) + '/' + str(pokemon_var.HP))

        
        
        print('')
        print('')
        print('')
        print('')
        print('')
        print(''+ self.spc6 + 'VOLTAR')
        print('escolha um pokemon'+ self.spc5)
        print('')
        section = input('')

        #filtro do que pode digitar
        if section != self.Voltar and section != self.pk2 and section != self.pk3 and section != self.pk4 and section != self.pk5 and section != self.pk6:
            section = self.Pokemon

        if section == self.Voltar:
            section = 'batalha'


        #Casso queira trocar de pokemon
        if section == self.pk2:
            if self.pokemon_2.NOME != 'Na':
                cont = self.pokemon_1
                

                self.pokemon_1 = self.pokemon_2
                self.pokemon_2 = cont

                

                section = 'batalha'
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()
            else:
                section = self.Pokemon
        
        if section == self.pk3:
            if self.pokemon_3.NOME != 'Na':
                cont = self.pokemon_1
                

                self.pokemon_1 = self.pokemon_3
                self.pokemon_3 = cont

                

                section = 'batalha'
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()
            else:
                section = self.Pokemon

        if section == self.pk4:
            if self.pokemon_4.NOME != 'Na':
                cont = self.pokemon_1
                

                self.pokemon_1 = self.pokemon_4
                self.pokemon_4 = cont

                

                section = 'batalha'
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()
            else:
                section = self.Pokemon

        if section == self.pk5:
            if self.pokemon_4.NOME != 'Na':
                cont = self.pokemon_1
                

                self.pokemon_1 = self.pokemon_5
                self.pokemon_5 = cont

                

                section = 'batalha'
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()
            else:
                section = self.Pokemon



        if section == self.pk6:
            if self.pokemon_6.NOME != 'Na':
                cont = self.pokemon_1
                

                self.pokemon_1 = self.pokemon_6
                self.pokemon_6 = cont

                

                section = 'batalha'
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()
            else:
                section = self.Pokemon





        return section

    def CORRER(self):
        
        if self.podeEscapar and self.escapar == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
            print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('' + self.spc3 + self.pokemon_1.NOME + '    Lvl ' + str(self.pokemon_1.LVL))
            print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
            print('')
            print('Voçê conseguiu' + self.spc7 + 'LUTAR'+ '    ' + 'MOCHILA')
            print('escapar' + self.spc8 + 'POKEMON' + '  ' + 'CORRER')
            print('')
            section = input('')

        if self.podeEscapar and self.escapar == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
            print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('' + self.spc3 + self.pokemon_1.NOME + '    Lvl ' + str(self.pokemon_1.LVL))
            print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
            print('')
            print('Voçê não conseguiu' + self.spc9 + 'LUTAR'+ '    ' + 'MOCHILA')
            print('escapar' + self.spc10 + 'POKEMON' + '  ' + 'CORRER')
            print('')
            section = input('')

        if not self.podeEscapar:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
            print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('' + self.spc3 + self.pokemon_1.NOME + '    Lvl ' + str(self.pokemon_1.LVL))
            print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
            print('')
            print('Voçê não pode' + self.spc11 + 'LUTAR'+ '    ' + 'MOCHILA')
            print('escapar dessa luta' + self.spc12 + 'POKEMON' + '  ' + 'CORRER')
            print('')
            section = input('')

        #filtro do que pode digitar
        if not self.podeEscapar or self.podeEscapar and self.escapar == 0:
            section = 'batalha'

        return section
    



    def intro(self):

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

    def exTurno(self):

        #essa função execulta o turno do inimigo

        self.turno = 'inimigo'


        #essa parte do codigo precisa muito ser comentada poos tem um nivel de complexidade medio
        #primeiro compara se esta no turno do inimigo e depois compara se o pokemon atual do
        #adversario possui vida maior que zero
        #apos isso o codigo sempre ira sortear um ataque para execultar, caso o ataque não
        #exista é sortea novamente o ataque
        # apos o sorteio ele pega o numero sorteado e junta ele com um sufixo e prefixo
        # "atk_" + str(ataque) + "_nome"  esse e a variavel que queremos acesar no objeto
        #
        #getattr(self.IN_pokemon_1, atk_nome) a função getattr funciona de um mmodo curioso
        
        if self.turno == 'inimigo' and self.IN_pokemon_1.HP_current > 0:

            while True:

                ataque = random.randint(1,4)
                atk_nome = "atk_" + str(ataque) + "_nome"
                atk_uso =  "atk_" + str(ataque) + "_uso"

                if getattr(self.IN_pokemon_1, atk_nome) != "---" and getattr(self.IN_pokemon_1, atk_uso) > 0:
                    
                    setattr(self.IN_pokemon_1, atk_uso, getattr(self.IN_pokemon_1, atk_uso) - 1)
                    self.text((self.IN_pokemon_1.NOME + ' usou'),getattr(self.IN_pokemon_1, atk_nome))
                    self.IN_pokemon_1.userSkill(getattr(self.IN_pokemon_1, atk_nome), self.pokemon_1)

                    self.turno = 'player'
                    break

    def text(self, t1,t2):

        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.IN_pokemon_1.NOME + '    Lvl ' + str(self.IN_pokemon_1.LVL))
        print('HP ' + str(self.IN_pokemon_1.HP_current) + '/' + str(self.IN_pokemon_1.HP))
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('' + self.spc3 + self.pokemon_1.NOME +'    Lvl ' + str(self.pokemon_1.LVL))
        print('' + self.spc3 + 'HP ' + str(self.pokemon_1.HP_current) + '/' + str(self.pokemon_1.HP))
        print('')
        print(t1)
        print(t2)
        print('')
        x = input('')

        #filtro do que pode digitar
        
    def update_invent(self):
        self.pk_invent.__class__.pokemon_1 = self.pokemon_1
        self.pk_invent.__class__.pokemon_2 = self.pokemon_2
        self.pk_invent.__class__.pokemon_3 = self.pokemon_3
        self.pk_invent.__class__.pokemon_4 = self.pokemon_4
        self.pk_invent.__class__.pokemon_5 = self.pokemon_5
        self.pk_invent.__class__.pokemon_6 = self.pokemon_6

    def __init__(self):


        Mus.Mus_p("ost/batlhe/Pokemon FireRed-LeafGreen Music- Wild Pokemon Battle (320 kbps).mp3")
        time.sleep(0.5)
        self.intro()


        import pokemon_inventory

        #chamando o inventario do jogador    acho que vou tirar isso depois
        self.pk_invent = pokemon_inventory.player_inventory()

        self.pokemon_1 = self.pk_invent.pokemon_1
        self.pokemon_2 = self.pk_invent.pokemon_2
        self.pokemon_3 = self.pk_invent.pokemon_3
        self.pokemon_4 = self.pk_invent.pokemon_4
        self.pokemon_5 = self.pk_invent.pokemon_5
        self.pokemon_6 = self.pk_invent.pokemon_6

        self.item_1 = self.pk_invent.item_1
        self.item_2 = self.pk_invent.item_2
        self.item_3 = self.pk_invent.item_3
        self.item_4 = self.pk_invent.item_4
        self.item_5 = self.pk_invent.item_5
        self.item_6 = self.pk_invent.item_6
        self.item_7 = self.pk_invent.item_7
        self.item_8 = self.pk_invent.item_8
        self.item_9 = self.pk_invent.item_9
        self.item_10 = self.pk_invent.item_10
        self.item_11 = self.pk_invent.item_11
        self.item_12 = self.pk_invent.item_12
        self.item_13 = self.pk_invent.item_13
        self.item_14 = self.pk_invent.item_14
        self.item_15 = self.pk_invent.item_15
        self.item_16 = self.pk_invent.item_16
        self.item_17 = self.pk_invent.item_17
        self.item_18 = self.pk_invent.item_18
        self.item_19 = self.pk_invent.item_19
        self.item_20 = self.pk_invent.item_20



        #chamando o inventario do inimigo
        self.IN_invent = pokemon_inventory.inimigo_inventory()

        self.IN_pokemon_1 = self.IN_invent.pokemon_1
        self.IN_pokemon_2 = self.IN_invent.pokemon_2
        self.IN_pokemon_3 = self.IN_invent.pokemon_3
        self.IN_pokemon_4 = self.IN_invent.pokemon_4
        self.IN_pokemon_5 = self.IN_invent.pokemon_5
        self.IN_pokemon_6 = self.IN_invent.pokemon_6


        #define quem começa primeiro
        if self.pokemon_1.SPEED > self.IN_pokemon_1.SPEED:
            self.turno = 'player'
        elif self.pokemon_1.SPEED < self.IN_pokemon_1.SPEED:
            self.turno = 'inimigo'
            self.exTurno()
        else:
            
            self.turno = random.randint(1,2)

            if self.turno == 1:
                self.turno = 'player'
                self.text(self.IN_invent.inimigo_name,'quer batalhar!')
                self.text(self.IN_invent.inimigo_name,('mandou ' + self.IN_pokemon_1.NOME))
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
            else:
                self.turno = 'inimigo'
                self.text(self.IN_invent.inimigo_name,'quer batalhar!')
                self.text(self.IN_invent.inimigo_name,('mandou ' + self.IN_pokemon_1.NOME))
                self.text(('Vá! ' + self.pokemon_1.NOME),'')
                self.exTurno()


        

        # fluxo principal do programa
        

        while self.inbatalhe == True:


            if self.pokemon_1.HP_current <= 0:

                
                if self.pokemon_2.HP_current <= 0 and self.pokemon_3.HP_current <= 0 and self.pokemon_4.HP_current <= 0 and self.pokemon_5.HP_current <= 0 and self.pokemon_6.HP_current <= 0:
                    self.inbatalhe = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("VOCÊ PERDEU")
                    
                else:
                    self.section = self.Pokemon


            if self.IN_pokemon_1.HP_current > 0:
                if self.section == 'batalha':
                    self.section = self.initBatalha()
                if self.section == self.Lutar:
                    self.section = self.LUTAR()
                if self.section == self.Pokemon:
                    self.section = self.POKEMON()
                if self.section == self.Mochila:
                    self.section = self.MOCHILA()
                if self.section == self.Correr:
                    self.section = self.CORRER()

            else:
                self.text(self.IN_pokemon_1.NOME,'Desmaia')
                self.text((self.pokemon_1.NOME + ' ganhou'),(str(self.IN_pokemon_1.XP) +' de Exp!'))
                

                self.pokemon_1.XP += self.IN_pokemon_1.XP

                if self.pokemon_1.check_xp(self.pokemon_1):
                    self.text(('HP = ' + str(self.pokemon_1.HP) + ' ATK = ' + str(self.pokemon_1.ATK) + ' DEF = ' + str(self.pokemon_1.DEF) ) , 'spATK = ' + str(self.pokemon_1.spATK) + ' spDEF = ' + str(self.pokemon_1.spDEF) + ' SPEED = ' + str(self.pokemon_1.SPEED))


                #troca o pokemon do inimigo
                for i in range(2,7):
                    pokemon_var = getattr(self, f"IN_pokemon_{i}")
                    

                    if pokemon_var.HP_current > 0:
                        cont = self.IN_pokemon_1
                        

                        self.IN_pokemon_1 = pokemon_var
                        pokemon_var = cont

                        
                        section = 'batalha'
                        self.text(('Vá! ' + self.IN_pokemon_1.NOME),'')
                
                if self.IN_pokemon_1.HP_current <= 0:
                    self.inbatalhe = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    Mus.Stop()
                    Mus.Mus_p("ost/win/Trainer Defeated! - Pokémon Ruby & Sapphire [High Quality] (320 kbps).mp3")
                    self.text('VOCÊ VENCEU','')
                    self.update_invent()
            
