import pygame
from random import choice


anim_move = [] # Список содержажий кадр анимации 


"""Анимация корабля """
for i in range(1, 11):
    filename = "imgs/enemy_ship{}.svg".format(i)
    img = pygame.image.load(filename)
    anim_move.append(img)


'''спавн корабля по иксу'''
spawn = []
for i in range(-430, 431):
    spawn.append(i)


def spawn_x():
    return choice(spawn)


class Enemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = anim_move[0]
        #self.image = pygame.image.load("work_images/enemy_ship1.svg") Если надо будет убрать анимацию, уберешь скобку
        self.speed = 0.3
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - choice(spawn)
        self.rect.bottom = self.screen_rect.bottom - 1200
        self.y = float(self.rect.y)
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70


    def moving_enemy(self):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= 1050:
            self.y = -150
            self.rect.centerx = self.screen_rect.centerx - spawn_x()

    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(anim_move):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = anim_move[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.screen.blit(self.image, self.rect)
        