import pygame
from styles import skin_1_anim,anim_skin2


class Skin_1():
    def __init__(self,screen): 
        self.screen = screen 
       # self.y = 200
        #self.x = 500
        self.img = pygame.transform.scale((skin_1_anim[0]),(250,250))
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70
        self.rect.centerx = self.screen_rect.centerx + 200
        self.rect.bottom = self.screen_rect.bottom - 600
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        
        
    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Надо переделать, для чистоты анимаци
                    
                    
            if self.frame >= len(skin_1_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.img = pygame.transform.scale(skin_1_anim[self.frame],(250, 250)).convert_alpha()
                self.rect = self.img.get_rect()
                self.rect.center = center
        
        self.screen.blit(self.img, self.rect)





class Skin_2():
    def __init__(self,screen): 
        self.screen = screen 
       # self.y = 200
        #self.x = 500
        self.img = pygame.transform.scale((anim_skin2[0]),(250,250))
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.frame = 0  # Номер кадра в списке anim, изначально равне 0
        self.last_update = pygame.time.get_ticks()  # Получаем последний кадр игры
        self.frame_rate = 70
        self.rect.centerx = self.screen_rect.centerx + 200
        self.rect.bottom = self.screen_rect.bottom - 300
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        
        
    def output(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Надо переделать, для чистоты анимаци
                    
                    
            if self.frame >= len(anim_skin2):
                self.frame = 0
            else:
                center = self.rect.center
                self.img = pygame.transform.scale(anim_skin2[self.frame],(250, 250)).convert_alpha()
                self.rect = self.img.get_rect()
                self.rect.center = center
        
        self.screen.blit(self.img, self.rect)
        
        
        