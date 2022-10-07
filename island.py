import pygame
from random import choice
from styles import anim_island

'''спавн острова по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


def spawn_x():
    return choice(spawn)




class Island():
    def __init__(self, screen):
        self.screen = screen
        #self.image = can
        self.image = anim_island[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.25
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1050
        self.y = float(self.rect.y)
        self.frame = 0 
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре

    def moving(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y == 1150:
            self.y = -100
            self.rect.centerx = self.screen_rect.centerx - spawn_x()

    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(anim_island):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = anim_island[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.screen.blit(self.image, self.rect)
