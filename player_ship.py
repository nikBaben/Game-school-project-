import pygame
from keys import movement
import keys
from gun import Gun
from styles import anim_fire, anim_ship
from styles import anim_shipplayer_moveup
from enemy_ship import Enemy
from submarine import Submarine


pic = pygame.image.load("imgs/ship_frame1.svg")
bullet = pygame.image.load("imgs/bullet.svg")

BLACK = (0, 0, 0)

'''АНИМАЦИЯ КОРАБЛЯ'''


class Player_Ship():
    def __init__(self, screen):
        self.screen = screen
        '''когда анимацию корабля будешь делать закомментишь'''
        self.image = anim_shipplayer_moveup[1].convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 60
        self.rect.bottom = self.screen_rect.bottom - 150
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        self.moveright = False
        self.moveleft = False
        self.moveup = False
        self.movedown = False
        self.sht = False  # Для выстрелов
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре
        self.speed = 1
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)

    def rocket(self, TF):
        print('1')
        if TF == 'True':
            print(2)
            if self.sht:
                print(3)
                return Enemy.death(), Submarine.death()

    def move(self):
        if self.moveright:
            if self.rect.centerx > 960:
                self.x = 0
            self.x += self.speed
        if self.moveleft:
            if self.rect.centerx < 0:
                self.x = 960
            self.x -= self.speed
        self.rect.x = self.x
        if self.moveup:
            if self.rect.bottom <= 150:
                self.moveup = False
                self.rect.y = 150
            else:
                self.y -= self.speed
        if self.movedown:
            if self.rect.bottom >= 1050:
                self.movedown = False
                self.rect.y = 1050
            else:
                self.y += self.speed
        self.rect.y = self.y

    def output(self):
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 130, 60, 130)
        # pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Надо переделать, для чистоты анимации

            if self.moveup:
                # self.frame +=1
                if self.frame >= len(anim_shipplayer_moveup):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_shipplayer_moveup[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

            if self.sht:
                if self.frame >= len(anim_fire):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_fire[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

            if self.moveright:
                if self.frame >= len(anim_fire):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_shipplayer_moveup[1]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

            if self.moveleft:
                if self.frame >= len(anim_shipplayer_moveup):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_shipplayer_moveup[1]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

            if self.moveleft == False and self.moveright == False and self.sht == False and self.moveup == False:
                if self.frame >= len(anim_shipplayer_moveup):
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = anim_shipplayer_moveup[1]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

        self.screen.blit(self.image, self.rect)
