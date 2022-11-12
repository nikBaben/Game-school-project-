import pygame
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first
from styles import anim_submarine

class Submarine():
    def __init__(self, screen):
        global sp
        self.screen = screen
        # self.image = (anim_enemy[0]).convert_alpha()
        self.image = (anim_submarine[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.35
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70  # Количесво кадров в игре
        sp = spawn_x()
        self.rect.centerx = 60 * sp
        # self.rect.bottom = self.screen_rect.bottom - 1200
        if spawn_check['submarine'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1350
            first('submarine')
        self.y = float(self.rect.y)
        self.hitbox = pygame.Rect((self.rect.centerx) - 26, (self.rect.bottom) - 195, 50, 190)

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
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame >= len(anim_submarine):
                    self.frame = 0
        else:
            center = self.rect.center
            self.image = anim_submarine[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
        self.screen.blit(self.image, self.rect)
        self.hitbox = pygame.Rect((self.rect.centerx) - 26, (self.rect.bottom) - 195, 50, 190)
        # pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
