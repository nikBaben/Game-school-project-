import pygame
from keys import movement
import keys
from gun import Gun
from styles import anim_fire, anim_ship
from styles import anim_shipplayer_moveup
from enemy_ship import Enemy
from submarine import Submarine
from styles import ainm_player_stand
from styles import player_move_up, anim_skin1, skin4, skin2, skin3
from skins import Skins_changer

# pic = pygame.image.load("imgs/ship_frame1.svg").convert_alpha()
# bullet = pygame.image.load("imgs/bullet.svg").convert_alpha()

BLACK = (0, 0, 0)
skins = Skins_changer()
'''АНИМАЦИЯ КОРАБЛЯ'''


class Player_Ship():
    def __init__(self, screen, freq):
        self.screen = screen
        self.skin1 = False
        self.skin2 = False
        self.skin3 = False
        self.changed = False
        self.image = (ainm_player_stand[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 60
        self.rect.bottom = self.screen_rect.bottom - 150
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        self.moveright = False
        self.moveleft = False
        self.moveup = False
        self.movedown = False
        self.sht = False  # Для выстрелов
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 60  # Количесво кадров в игре
        if freq == 60:
            self.speed = 7
        if freq == 144:
            self.speed = 4
        else:
            self.speed = 6
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 145, 60, 130)
        self.have_rocket = False

    def move(self):

        if self.moveright:
            if self.rect.centerx > 960:
                self.x = -75
            self.x += self.speed
        if self.moveleft:
            if self.rect.centerx < 0:
                self.x = 915
            self.x -= self.speed
        self.rect.x = self.x
        if self.moveup:
            if self.rect.bottom <= 150:
                self.moveup = False
                self.rect.y = 150
            else:
                self.y -= self.speed
        if self.movedown:
            if self.rect.bottom >= 1050:
                self.movedown = False
                self.rect.y = 1050
            else:
                self.y += self.speed
        self.rect.y = self.y

    def output(self):
        self.hitbox = pygame.Rect((self.rect.centerx) - 30, (self.rect.bottom) - 130, 60, 130)
        # pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Надо переделать, для чистоты анимаци
            if self.changed:
                if self.skin1:

                    if self.moveup:
                        # self.frame +=1
                        if self.frame >= len(player_move_up):
                            self.frame = 0
                        else:
                            center = self.rect.center
                            self.image = (player_move_up[self.frame]).convert_alpha()
                            self.rect = self.image.get_rect()
                            self.rect.center = center

                    if self.sht:
                        if self.frame >= len(anim_fire):
                            self.frame = 0
                        else:
                            center = self.rect.center
                            self.image = (anim_fire[self.frame]).convert_alpha()
                            self.rect = self.image.get_rect()
                            self.rect.center = center

                    if self.moveright:
                        if self.frame >= len(anim_fire):
                            self.frame = 0
                        else:
                            center = self.rect.center
                            self.image = (player_move_up[1]).convert_alpha()
                            self.rect = self.image.get_rect()
                            self.rect.center = center

                    if self.moveleft:
                        if self.frame >= len(anim_shipplayer_moveup):
                            self.frame = 0
                        else:
                            center = self.rect.center
                            self.image = (player_move_up[1]).convert_alpha()
                            self.rect = self.image.get_rect()
                            self.rect.center = center

                    if self.moveleft == False and self.moveright == False and self.sht == False and self.moveup == False and self.movedown == False:
                        if self.frame >= len(ainm_player_stand):
                            self.frame = 0
                        else:
                            center = self.rect.center
                            self.image = (ainm_player_stand[self.frame]).convert_alpha()
                            self.rect = self.image.get_rect()
                            self.rect.center = center

                    # self.image = (ainm_player_stand[0]).convert_alpha()
                if self.skin2:
                    self.image = skin2.convert_alpha()
                if self.skin3:
                    self.image = skin3.convert_alpha()

            # if self.frame >= len(anim_skin1):
            #    self.frame = 0
            # else:
            #    center = self.rect.center
            #  self.image = (anim_skin1[self.frame]).convert_alpha()
            # self.rect = self.image.get_rect()
            #  self.rect.center = center

            else:
                if self.moveup:
                    # self.frame +=1
                    if self.frame >= len(player_move_up):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = (player_move_up[self.frame]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center

                if self.sht:
                    if self.frame >= len(anim_fire):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = (anim_fire[self.frame]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center

                if self.moveright:
                    if self.frame >= len(anim_fire):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = (player_move_up[1]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center

                if self.moveleft:
                    if self.frame >= len(anim_shipplayer_moveup):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = (player_move_up[1]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center

                if self.moveleft == False and self.moveright == False and self.sht == False and self.moveup == False and self.movedown == False:
                    if self.frame >= len(ainm_player_stand):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = (ainm_player_stand[self.frame]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center

        self.screen.blit(self.image, self.rect)
