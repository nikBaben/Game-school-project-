import pygame


class Blow():
    def __init__(self, screen):
        self.screen = screen
        self.width = 100
        self.height = 100
        self.visible = True
        self.rect = pygame.Rect(0,0,self.width,self.height)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
