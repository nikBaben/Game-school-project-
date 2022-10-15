import pygame
from styles import anim_can
from spawn import spawn_x, cords
from spawn import spawn_check, first


class Can():
    def __init__(self, screen):
        global sp
        self.screen = screen
        self.image = anim_can[0].convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.5
        sp = spawn_x()
        self.rect.centerx = 60 * sp
        # self.rect.bottom = self.screen_rect.bottom - 1100
        if spawn_check['can'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1700
            first('can')
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре
        self.hitbox = ((self.rect.centerx) - 60, (self.rect.bottom) - 150, 120,
                       150)  # Параметры хит бокса, можно протестить в функции output

    def moving_can(self):
        global sp
        self.y += self.speed
        self.rect.y = self.y

        if self.y == 1100:
            self.y = -50
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp

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
