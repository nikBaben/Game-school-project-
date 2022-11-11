import pygame
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first


class Submarine():
    def __init__(self, screen):
        global sp
        self.screen = screen
        # self.image = (anim_enemy[0]).convert_alpha()
        self.image = pygame.image.load('work_images/sub1.svg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.35
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        sp = spawn_x()
        self.rect.centerx = 60 * sp
        # self.rect.bottom = self.screen_rect.bottom - 1200
        if spawn_check['submarine'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1350
            first('submarine')
        self.y = float(self.rect.y)

    def moving_sub(self):
        global sp
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= 1050:
            self.y = -220
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp

    def death(self):
        global sp
        self.y = -600
        cords[sp] = True
        sp = spawn_x()
        self.rect.centerx = 60 * sp

    def output(self):
        self.screen.blit(self.image, self.rect)
