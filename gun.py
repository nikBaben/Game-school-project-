import pygame


class Gun(pygame.sprite.Sprite):
    def __init__(self, screen, player_ship):
        super(Gun, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        '''ПУЛЯ'''
        self.hit = player_ship.hit()
        # self.image = pygame.image.load("imgs/bullet.svg")
        self.image = pygame.image.load("work_images/pulya.png")
        self.speed = 2
        self.rect.centerx = player_ship.rect.centerx
        self.rect.top = player_ship.rect.top + 25
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def output_bullet(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, self.rect)
        # pygame.blit(self.image)
