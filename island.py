import pygame
from random import choice
from styles import anim_island
from spawn import spawn_x, cords


class Island():
    def __init__(self, screen):
        global sp, sp1, sp2
        self.screen = screen
        # self.image = can
        self.image = anim_island[0].convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.25
        sp = spawn_x()
        sp1, sp2 = sp - 1, sp + 1
        cords[sp1] = False
        cords[sp2] = False
        self.rect.centerx = 60 * sp
        self.rect.bottom = self.screen_rect.bottom - 1050
        self.y = float(self.rect.y)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре

    def moving(self):
        global sp, sp1, sp2
        self.y += self.speed
        self.rect.y = self.y

        if self.y == 1150:
            self.y = -200
            cords[sp] = True
            cords[sp1] = True
            cords[sp2] = True
            sp = spawn_x()
            sp1, sp2 = sp - 1, sp + 1
            cords[sp1] = False
            cords[sp2] = False
            self.rect.centerx = 60 * sp

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
