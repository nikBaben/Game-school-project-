import pygame
from random import choice
from styles import anim_can

'''спавн бочки по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


def spawn_x():
    return choice(spawn)


class Can():
    def __init__(self, screen):
        self.screen = screen
        self.image = anim_can[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.5
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1100
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре
        self.hitbox = ((self.rect.centerx) -60 ,(self.rect.bottom)-150,120,150) # Параметры хит бокса, можно протестить в функции output 

    def moving_can(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y == 1100:
            self.y = -50
            self.rect.centerx = self.screen_rect.centerx - spawn_x()

    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(anim_can):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = anim_can[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

        self.screen.blit(self.image, self.rect)
