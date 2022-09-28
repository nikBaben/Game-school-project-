import pygame

BLACK = (0, 0, 0)
anim_stand = []
anim_move = []
for i in range (1,14): 
    filename = "imgs/ship_frame{}.svg".format(i)
    img  = pygame.image.load(filename)
   # img.set_colorkey(BLACK)
    anim_stand.append(img)


#for j in range(1,10): 
  #  filename = "imgs/ship_motion{}.svg".format(i)
    #img = pygame.image.load(filename)
    #img.set_colorkey(BLACK)
   # anim_move.apend(img)



class Player_Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = anim_stand[0]
        self.rect = self.image.get_rect()
       # self.image = pygame.image.load("imgs/хуй{0}".fromat(name))
       # self.rect = self.image()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False
        self.moveup = False
        self.movedown = False
        self.frame = 0 # Номер кадра в списке anim, изначально равне 0 
        self.last_update = pygame.time.get_ticks() # Получаем последний кадр игры 
        self.frame_rate = 70 # Количесво кадров в игре


    def move(self):
        if self.moveright:
            if self.rect.centerx > 960:
                self.rect.centerx = 0
            self.rect.centerx += 3
            
            #self.image = pygame.Surface((1000, 1000))   
            #self.image  = pygame.image.load("imgs/bullet.svg")
    
          


        if self.moveleft:
            if self.rect.centerx < 0:
                self.rect.centerx = 960
            self.rect.centerx -= 3
        if self.moveup:
            if self.rect.bottom <= 150:
                self.moveup = False
                self.rect.bottom = 150
            self.rect.bottom -= 3
        if self.movedown:
            if self.rect.bottom >= 1050:
                self.movedown = False
                self.rect.bottom = 1050
            self.rect.bottom += 3

    def output(self):
        now = pygame.time.get_ticks() 
        if now - self.last_update > self.frame_rate: 
            self.last_update = now
            self.frame += 1
            if self.frame == len(anim_stand):
               self.frame = 0 
            else:
                center = self.rect.center
                self.image = anim_stand[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.screen.blit(self.image, self.rect)
