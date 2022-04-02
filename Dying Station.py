

import pygame
from sys import exit 

pygame.mixer.init()
pygame.init() 
screen = pygame.display.set_mode((1000,1000), pygame.RESIZABLE)
pygame.display.set_caption('Dying Station')
clock = pygame.time.Clock()


terminal = pygame.image.load('terminal.png').convert()
floor = pygame.image.load('floor.png').convert()
purifyer = pygame.image.load('purifyer.png').convert()

terminal_rect = terminal.get_rect(center =(500,500))



screen.blit(floor, (0,0))
screen.blit(terminal, terminal_rect)
screen.blit(purifyer, (1,51))







class SpaceMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Space.png').convert_alpha()
        self.rect =self.image.get_rect(midbottom = (400,400))
        self.direction = pygame.math.Vector2()
        self.speed = 5

    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.KEY_UP]:
            self.direction.y = -1
        elif keys[pygame.KEY_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0


        if keys[pygame.KEY_LEFT]:
            self.direction.x = -1
        elif keys[pygame.KEY_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self,speed):
        self.rect.center += self.direction * speed
    def update(self):
        self.input()
        self.move(self.speed)
        

spaceman = pygame.sprite.GroupSingle()
spaceman.add(SpaceMan())
spaceman.draw(screen)
    
    
    
   




music = pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)
repair_sound = pygame.mixer.Sound("repair.wav")





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            

   
    #if event.type == pygame.KEYDOWN:
               # if event.key == pygame.K_LEFT or event.key == ord('a'):
                    #SpaceMan.control(steps,0)
                #if event.key == pygame.K_RIGHT or event.key == ord('d'):
                   #print('right')
               # if event.key == pygame.K_UP or event.key == ord('w'):
                    #print('up')
                #if event.key == pygame.K_DOWN or event.key == ord('s'):
                    #print('down') 
               # if event.key == pygame.K_LCTRL:
                   # print('repair')
                    #repair_sound.play()


    


       






       
       



        pygame.display.update()
        clock.tick(69)