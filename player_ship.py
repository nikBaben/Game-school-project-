import pygame
from keys import movement
import keys 
from gun import Gun
from styles import anim_fire, anim_ship


pic = pygame.image.load("imgs/ship_frame1.svg")
bullet = pygame.image.load("imgs/bullet.svg")

BLACK = (0, 0, 0)


'''АНИМАЦИЯ КОРАБЛЯ'''





class Player_Ship():
    def __init__(self, screen):
        self.screen = screen
        '''когда анимацию корабля будешь делать закомментишь'''
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
        self.hitbox = ((self.rect.centerx) -60 ,(self.rect.bottom)-150,120,150) # Параметры хит бокса, можно протестить в функции output 

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
           
    def hit (self): 
        pass
      
             #   if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y<enemy.hitbox[1] + enemy.hitbox[3]:
               #     print("hit")



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
        self.hitbox  = ((self.rect.centerx) - 35,(self.rect.bottom) - 130,70,130) # Отрисовываю хит бокс для теста
        pygame.draw.rect(self.screen, (0,0,0), self.hitbox,1 )
