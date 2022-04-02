import pygame
from sys import exit 


class SpaceMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Space.png').convert_alpha()
        self.rect =self.image.get_rect(midbottom = (510,590))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('walk')



pygame.mixer.init()
pygame.init() 
screen = pygame.display.set_mode((1000,1000), pygame.RESIZABLE)
pygame.display.set_caption('Dying Station')
clock = pygame.time.Clock()





#Map items and maps
terminal = pygame.image.load('terminal.png').convert()
floor = pygame.image.load('floor.png').convert()
purifyer = pygame.image.load('purifyer.png').convert()

#map items rects
terminal_rect = terminal.get_rect(center =(500,500))
#purifyer_rect = purifyer.get_(center =(0,1000))

#music and SFX
music = pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            

   
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up')
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down') 
                if event.key == pygame.K_LCTRL:
                    print('repair')



    

#backrounds 
    screen.blit(floor, (0,0))
    screen.blit(terminal, terminal_rect)
    screen.blit(purifyer, (1,51))





#player
    spaceman = pygame.sprite.GroupSingle()
    spaceman.add(SpaceMan())
    spaceman.draw(screen)



    pygame.display.update()
    clock.tick(69)