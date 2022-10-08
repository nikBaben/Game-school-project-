import pygame


class Sub_gun(pygame.sprite.Sprite):
    def __init__(self, screen, submarine):
        super(Sub_gun, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        '''ПУЛЯ'''
        # self.image = pygame.image.load("imgs/bullet.svg")
        self.image = pygame.image.load("work_images/torpeda.png")
        self.speed = 0.75
        self.rect.centerx = submarine.rect.centerx
        self.rect.top = submarine.rect.top + 125
        self.y = float(self.rect.y)

    def update(self, submarine):
        self.y += self.speed
        self.rect.y = self.y

        if self.y >= (submarine.rect.bottom + 700):
            self.y = submarine.rect.bottom
            self.rect.centerx = submarine.rect.centerx

    def output_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, self.rect)
        # pygame.blit(self.image)
