import pygame


class Gun(pygame.sprite.Sprite):
    def __init__(self, screen, player_ship, freq):
        global rect
        super(Gun, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        '''ПУЛЯ'''
        self.image = pygame.image.load("imgs/bullet.svg").convert_alpha()
        if freq <= 60:
            self.speed = 25
        if freq >= 120:
            self.speed = 10
        else:
            self.speed = 18
        self.rect.centerx = player_ship.rect.centerx
        self.rect.top = player_ship.rect.top + 25
        self.y = float(self.rect.y)

    def position(self):
        return self.rect.y

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def output_bullet(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, (0,0,0), self.rect, 1)
