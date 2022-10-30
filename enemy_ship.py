import pygame
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = (anim_enemy[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        global sp
        self.speed = 0.3
        sp = spawn_x()
        self.rect.centerx = 60 * sp
        self.rect.bottom = self.screen_rect.bottom - 1200
        if spawn_check['ship'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1400
            first('ship')
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70
        self.flag = False
        self.hitbox = ((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)

    def moving_enemy(self):
        global sp
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= 1050:
            self.y = -150
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp

    def death(self):
        global sp
        self.y = -500
        cords[sp] = True
        sp = spawn_x()
        self.rect.centerx = 60 * sp

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.hitbox = ((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)  # Отрисовываю хит бокс для теста
        pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
