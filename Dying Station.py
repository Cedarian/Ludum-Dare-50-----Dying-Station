import pygame
from sys import exit 


class SpaceMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Space.png').convert_alpha()
        self.rect =self.image.get_rect(midbottom = (300,300))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('walk')


pygame.init() 
screen = pygame.display.set_mode((1000,1000)) 
pygame.display.set_caption('Dying Station')
clock = pygame.time.Clock()

terminal = pygame.image.load('terminal.png').convert()
floor = pygame.image.load('floor.png').convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    






#backrounds 
    screen.blit(floor, (0,0))
    screen.blit(terminal,(501,500))





#player
    spaceman = pygame.sprite.GroupSingle()
    spaceman.add(SpaceMan())
    spaceman.draw(screen)

















    pygame.display.update()
    clock.tick(69)