import pygame
from random import choice

'''спавн бочки по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


class Can():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("work_images/can.png")
        self.speed = 0.5
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1100
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def moving_can(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y == 1100:
            self.y = -50

    def output(self):
        self.screen.blit(self.image, self.rect)
