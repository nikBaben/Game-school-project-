# import pygame
# from enemy_ship import Enemy
# from pygame.sprite import Sprite
#
#
# class Dead_Enemy(Enemy, Sprite):
#     def __init__(self, screen, enemy):
#         super(Enemy, self).__init__()
#         self.image = pygame.image.load('work_images/dead_enemy.png')
#         self.screen_rect = screen.get_rect()
#         self.rect.bottom = enemy.rect.bottom
#
#     def output(self):
#         self.screen.blit(self.image, self.rect)
