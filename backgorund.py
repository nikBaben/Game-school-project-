from styles import back_ground, back_ground2
import math


class Back():
    def __init__(self, screen):
        self.screen = screen
        self.image = back_ground.convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.y = self.rect.y
        self.speed = 0.3
    def scroling (self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top == 1050:
            self.y = 0
    def output_back(self):
        self.screen.blit(self.image,self.rect)


class Back2():
    def __init__(self, screen):
        self.screen = screen
        self.image = back_ground2.convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.y = -1050
        self.speed = 0.3
    def down(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top == 0:
            self.y = -1050
    def output_back2(self):
        self.screen.blit(self.image,self.rect)


