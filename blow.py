import pygame


class Blow():
    def __init__(self, screen):
        self.screen = screen
        self.width = 100
        self.height = 100
        self.visible = True
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def draw(self, image):
        self.image = ''
        if image == 'ship':
            self.image = pygame.image.load('work_images/blow_ship.png')
        if image == 'sub':
            self.image = pygame.image.load('work_images/blow_sup.png')
        if image == 'can':
            self.image = pygame.image.load('work_images/blow_can.png')
        self.screen.blit(self.image, self.rect)
