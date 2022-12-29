import pygame
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first
from pygame.sprite import Sprite
from styles import blow_ship_anim


class Enemy(Sprite):
    def __init__(self, screen, freq):
        super().__init__()
        global sp
        self.screen = screen
        self.image = (anim_enemy[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        if freq <= 60:
            self.speed = 4.8
        if freq >= 120:
            self.speed = 2.3
        else:
            self.speed = 4.5
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Номер кадра в списке anim, изначально равне 0
        self.last_update1 = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate1 = 70  # Количесво кадров в игре
        self.dead = False
        self.blow = False
        self.hit = False
        self.frame_blow = 0
        self.y_True = True

        sp = spawn_x()
        self.rect.centerx = 60 * sp
        self.rect.bottom = self.screen_rect.bottom - 1200
        if spawn_check['ship'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1400
            first('ship')
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 90
        self.flag = False
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)

    def moving_enemy(self):
        global sp
        if self.y_True == True:
            self.y += self.speed
            self.rect.y = self.y

        if self.y >= 1050:
            self.y = -150
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp

    def death(self):
        global sp
        self.y = -350
        cords[sp] = True
        sp = spawn_x()
        self.rect.centerx = 60 * sp
        self.hit = False
        self.dead = False
        self.blow = False

    def output(self):
        now = pygame.time.get_ticks()
        now1 = pygame.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1

            if self.frame >= len(anim_enemy):
                self.frame = 0

            else:
                center = self.rect.center
                self.image = (anim_enemy[self.frame]).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = center

            if self.blow == True and self.dead == False:

                if now1 - self.last_update1 > self.frame_rate1:
                    self.last_update1 = now1
                    self.frame_blow += 1

                    if self.frame_blow >= len(blow_ship_anim):
                        self.frame_blow = 0
                        self.blow = False
                        self.dead = True
                        self.hit = True
                        self.y_True = True

                    else:
                        center = self.rect.center
                        self.image = (blow_ship_anim[self.frame_blow]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center
                        self.y_True = False

        self.screen.blit(self.image, self.rect)
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60,
                                  130)  # Отрисовываю хит бокс для теста
        # pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
