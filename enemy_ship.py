import pygame
from random import choice

'''спавн корабля по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


def spawn_x():
    return choice(spawn)


class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("work_images/enemy_work.png")
        self.speed = 0.3
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1200
        self.y = float(self.rect.y)

    def moving_enemy(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= 1050:
            self.y = -150
            self.rect.centerx = self.screen_rect.centerx - spawn_x()

    def output(self):
        self.screen.blit(self.image, self.rect)
