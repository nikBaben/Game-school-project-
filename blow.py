import pygame
from styles import blow_can_anim,blow_sub_anim,blow_ship_anim
from submarine import Submarine
from enemy_ship import Enemy
class Blow():
    def __init__(self, screen):
        self.screen = screen
        self.width = 100
        self.height = 100
        self.visible = True
       # self.image =""
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # К
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def draw(self, image):
        now = pygame.time.get_ticks()
        self.image = ''
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Надо 
            if image == 'can':
                if self.frame >= len(blow_can_anim):
                    self.frame = 0
                 #  Submarine.death()
                else:
                    self.image = (blow_can_anim[1])
                    self.screen.blit(self.image, self.rect)
            if image == 'ship':
                if self.frame >= len(blow_ship_anim):
                    self.frame = 0
                    #Enemy.death(Enemy)
                else:
                    self.image = (blow_ship_anim[self.frame])
                    self.screen.blit(self.image, self.rect)
                   
            if image == 'sub':
                if self.frame >= len(blow_sub_anim):
                    self.frame = 0
                    #Submarine.death(Submarine)
                else:
                    self.image = (blow_sub_anim[self.frame])
                    self.screen.blit(self.image, self.rect)
            else: 
                pass
           
                 
            # self.rect = self.image.get_rect()
               # self.rect.center = center
                #self.image = pygame.image.load('imgs/blow_can.svg').convert_alpha()
               # self.image = pygame.image.load('work_images/blow_sup.png').convert_alpha()
       
         #   if self.frame >= len(blow_can_anim):
                   # self.frame = 0
         #   else:
               # center = self.rect.center
             #   self.image = (blow_can_anim[self.frame]).convert_alpha()
               # self.rect = self.image.get_rect()
               # self.rect.center = center
                #self.image = pygame.image.load('imgs/blow_can.svg').convert_alpha()
       # self.screen.blit(self.image, self.rect)
