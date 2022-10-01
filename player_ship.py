import pygame
from keys import movement

import keys 
pic = pygame.image.load("imgs/ship_frame1.svg")
bullet = pygame.image.load("imgs/bullet.svg")

BLACK = (0, 0, 0)
anim_fire = []
anim_ship = []

'''АНИМАЦИЯ КОРАБЛЯ'''


for j in range(1,13):
    filename = "imgs/fire_player_ship{}.svg".format(j)
    img = pygame.image.load(filename)
  
    anim_fire.append(img)

for i in range(1,15):
    file =  "imgs/ship_frame{}.svg".format(i)
    im = pygame.image.load(file)
  
    anim_ship.append(im)



class Player_Ship():
    def __init__(self, screen):
        self.screen = screen
  
        '''когда анимацию корабля будешь делать закомментишь'''
         # Количесво кадров в игр
        #self.image = pygame.image.load("work_images/ship_work.png")
        self.image = anim_ship[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False
        self.moveup = False
        self.movedown = False
        self.sht = False# Для выстрелов
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре

    def move(self):
        if self.moveright:
            if self.rect.centerx > 960:
                self.rect.centerx = 0
            self.rect.centerx += 1
        if self.moveleft:
            if self.rect.centerx < 0:
                self.rect.centerx = 960
            self.rect.centerx -= 1
            """ Доделат!!!! Просто поле для проверки, что все работает) """
            self.image  = bullet # Меняет кадр, если нажата клавиша "A" ef
            """"""
        if self.moveup:
            if self.rect.bottom <= 150:
                self.moveup = False
                self.rect.bottom = 150
            self.rect.bottom -= 1
        if self.movedown:
            if self.rect.bottom >= 1050:
                self.movedown = False
                self.rect.bottom = 1050
            self.rect.bottom += 1
        if self.sht:
            """Доделать!!!! Просто поле для проверки что все рабоатет)"""
            self.image = anim_fire[0] # Меняет кадр, если нажата клавиша "F"
            """"""
           



    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.sht:
                if self.frame >= len(anim_fire):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_fire[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
            else: 
                if self.frame >= len(anim_ship):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_ship[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
            
                
        self.screen.blit(self.image, self.rect)
