import pygame
from enemy_ship import Enemy


class Enemy_gun(pygame.sprite.Sprite):
    def __init__(self, screen, enemy_ship, freq):
        super(Enemy_gun, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        '''ПУЛЯ'''
        # self.image = pygame.image.load("imgs/bullet.svg")
        self.image = pygame.image.load("imgs/bullet.svg").convert_alpha()
        if freq <= 60:
            self.speed = 20
        if freq >= 120:
            self.speed = 8
        else:
            self.speed = 16
        self.rect.centerx = enemy_ship.rect.centerx
        self.rect.top = enemy_ship.rect.top + 125
        self.y = float(self.rect.y)

    def update(self, enemy_ship):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= (enemy_ship.rect.bottom + 1060):
            self.y = enemy_ship.rect.bottom
            self.rect.centerx = enemy_ship.rect.centerx

    def shot(self, enemy_ship):
        self.y = enemy_ship.rect.bottom
        self.rect.centerx = enemy_ship.rect.centerx

    def death(self, enemy_ship):
        self.y = enemy_ship.rect.bottom
        self.rect.centerx = enemy_ship.rect.centerx

    def output_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, self.rect)
        # pygame.blit(self.image)
