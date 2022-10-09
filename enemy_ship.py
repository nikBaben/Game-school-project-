import pygame
from random import choice

import player_ship
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first


class Enemy():
    def __init__(self, screen):
        global sp
        self.screen = screen
        self.image = (anim_enemy[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 0.3
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
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

        # pos = player_ship.Player_Ship.pos()
        # if self.rect.colliderect(pos):
        #     print('1')

        # if self.rect.colliderect(self, player_ship.position()):
        #     self.y = -300
        #     cords[sp] = True
        #     sp = spawn_x()
        #     self.rect.centerx = 60 * sp

    def enemy_update(enemy):
        pass  # Я забыл  зачем создавал эта функция, ЪХАХАХАХАХ, мб пригодится

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.hitbox = ((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)  # Отрисовываю хит бокс для теста
        pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
