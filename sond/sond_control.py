<<<<<<< HEAD

import pygame
import keyboard


class Mus:
    def __init__(self):
        self.music = ''
    
    def Mus_p(self,mus):
            #mixer do pygame
            pygame.mixer.init()
            self.music = pygame.mixer.Sound(mus)
            self.music.play()

    def Stop(self):
         self.music.stop()






def on_key(event):
    if event.name == 'enter' and event.event_type == 'down':
        pygame.mixer.music.load("ost/Fx/Pokemon (A Button) - Sound Effect (HD) (320 kbps).mp3")
        pygame.mixer.music.play()

        
        # Mantém o programa em execução
        #keyboard.wait()


=======

import pygame
import keyboard


class Mus:
    def __init__(self):
        self.music = ''
    
    def Mus_p(self,mus):
            #mixer do pygame
            pygame.mixer.init()
            self.music = pygame.mixer.Sound(mus)
            self.music.play()

    def Stop(self):
         self.music.stop()






def on_key(event):
    if event.name == 'enter' and event.event_type == 'down':
        pygame.mixer.music.load("ost/Fx/Pokemon (A Button) - Sound Effect (HD) (320 kbps).mp3")
        pygame.mixer.music.play()

        
        # Mantém o programa em execução
        #keyboard.wait()


>>>>>>> da22c5d3b9fdadea95ca37c6fb899ba889e6a480
keyboard.on_press(on_key)