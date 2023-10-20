import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Exemplo de Sprite com Pygame")

# Carregamento do sprite
original_sprite_image = pygame.image.load("D:\diretorio de trabalho\CRIAÇÃO DE JOGOS\poskemon\graphics\Menus\Teste1.png")  
original_sprite_width, original_sprite_height = original_sprite_image.get_size()

sprite_image = pygame.transform.scale(original_sprite_image, (screen_width, screen_height))

sprite_rect = sprite_image.get_rect()
sprite_rect.center = (screen.get_width() // 2, screen.get_height() // 2)



HUD1player = pygame.image.load("D:\diretorio de trabalho\CRIAÇÃO DE JOGOS\poskemon\graphics\Menus\HUD1.png")  
HUD1player_rect = HUD1player.get_rect()
HUD1player_rect.center = (screen.get_width() // 2, screen.get_height() // 2)



# Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualização da tela
    screen.fill((255, 255, 255))  # Preenche a tela com branco
    screen.blit(sprite_image, sprite_rect)  # Desenha o sprite na tela

    screen.blit(HUD1player, HUD1player_rect)  # Desenha o sprite na tela
    pygame.display.flip()  # Atualiza a tela

    clock.tick(60)  # Limite de quadros por segundo

# Encerramento do Pygame
pygame.quit()
sys.exit()