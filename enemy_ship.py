import pygame
from random import choice
from styles import anim_ship
'''спавн корабля по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


def spawn_x():
    return choice(spawn)

anim_enemy=[]
for j in range(1,11):
    filename = "imgs/enemy_ship{}.svg".format(j)
    img = pygame.image.load(filename)
  
    anim_enemy.append(img)

class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = anim_enemy[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.3
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1200
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70
        self.flag  = False
        self.hitbox = ((self.rect.centerx) -60 ,(self.rect.bottom)-150,120,150)


    def moving_enemy(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= 1050:
            self.y = -150
            self.rect.centerx = self.screen_rect.centerx - spawn_x()
      
    def enemy_update(enemy): 
        pass# Я забыл  зачем создавал эта функция, ЪХАХАХАХАХ, мб пригодится


    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(anim_enemy):
                    self.frame = 0
            else:
                center = self.rect.center
                self.image = anim_enemy[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.screen.blit(self.image, self.rect)
        self.hitbox  = ((self.rect.centerx) - 35,(self.rect.bottom) - 130,120,140) # Отрисовываю хит бокс для теста
        pygame.draw.rect(self.screen, (0,0,0), self.hitbox,1 )
