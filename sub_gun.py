import pygame


class Sub_gun(pygame.sprite.Sprite):
    def __init__(self, screen, submarine, freq):
        super(Sub_gun, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        '''ПУЛЯ'''
        # self.image = pygame.image.load("imgs/bullet.svg")
        self.image = pygame.image.load("work_images/bulet_for_sub.svg").convert_alpha()
        if freq <= 60:
            self.speed = 12
        if freq >= 120:
            self.speed = 4.3
        else:
            self.speed = 11

        self.rect.centerx = submarine.rect.centerx
        self.rect.top = submarine.rect.top + 125
        self.y = float(self.rect.y)
        self.start_pos = False

    def update(self, submarine):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= (submarine.rect.bottom + 700):
            self.y = submarine.rect.bottom
            self.rect.centerx = submarine.rect.centerx

    def shot(self, enemy_ship):
        self.y = enemy_ship.rect.bottom
        self.rect.centerx = enemy_ship.rect.centerx

    def death(self, submarine):
        self.y = submarine.rect.bottom
        self.rect.centerx = submarine.rect.centerx

    def output_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, self.rect)
        # pygame.blit(self.image)
