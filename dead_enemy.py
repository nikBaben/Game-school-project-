# import pygame
#
#
# class Dead_enemy(pygame.sprite.Sprite):
#     def __init__(self, screen, enemy_ship):
#         super(Dead_enemy, self).__init__()
#         self.screen = screen
#         self.image = pygame.image.load("work_images/dead_enemy.png")
#         self.rect.centerx = enemy_ship.rect.centerx
#         self.rect.top = enemy_ship.rect.top
#
#     def stop(self):
#         self.rect.top = 500
#
#     def output_enemy_bullet(self):
#         self.screen.blit(self.image, self.rect)
