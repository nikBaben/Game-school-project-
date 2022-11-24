import pygame
from styles import anim_ship, anim_enemy
from spawn import spawn_x, cords
from spawn import spawn_check, first
from styles import anim_submarine
from styles import blow_sub_anim
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
        self.last_update = pygame.time.get_ticks()
        self.last_update1 = pygame.time.get_ticks() # Получаем последний кадр игры
        self.frame_rate = 70
        self.frame_rate1 = 70  # Количесво кадров в игре
        sp = spawn_x()
        self.dead = False
        self.blow = False
        self.hit = False
        self.frame_blow = 0 
        self.y_True = True
       # self.tp = False
        self.rect.centerx = 60 * sp
        # self.rect.bottom = self.screen_rect.bottom - 1200
        if spawn_check['submarine'] == False:
            self.rect.bottom = self.screen_rect.bottom - 1350
            first('submarine')
        self.y = float(self.rect.y)
        self.hitbox = pygame.Rect((self.rect.centerx) - 26, (self.rect.bottom) - 195, 50, 190)

    def moving_sub(self):
        global sp
        if self.y_True == True:
            self.y += self.speed
            self.rect.y = self.y

        if self.y >= 1050:
            self.y = -220
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp
            
    def death(self): 
        #if self.dead == True:
            global sp
           # self.y +=2
            self.y = -600
            cords[sp] = True
            sp = spawn_x()
            self.rect.centerx = 60 * sp
            self.hit = False
            self.dead = False
            self.blow = False
         #   self.blow = False
        #else: pass
        #self.blow = False
        #self.tp = False

    def output(self):
        now = pygame.time.get_ticks()
        now1 = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(anim_submarine):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = (anim_submarine[self.frame]).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = center
        

            if self.blow == True and self.dead == False: 
                if now1 - self.last_update1 > self.frame_rate1:
                    self.last_update1 = now1
                    self.frame_blow += 1
                    if self.frame_blow >= len(blow_sub_anim):
                        self.frame_blow = 0
                        self.blow  = False
                        self.dead = True
                        self.hit = True
                        self.y_True = True
                       # self.speed = 0.35
                       
                   
                    else:
                        center = self.rect.center
                        self.image = (blow_sub_anim[self.frame_blow]).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = center
                        self.y_True = False
                      #  self.speed =  0

        self.hitbox = pygame.Rect((self.rect.centerx) - 26, (self.rect.bottom) - 195, 50, 190)
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 1)
