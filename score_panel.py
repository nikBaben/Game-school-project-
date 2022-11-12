import pygame


class Score_panel():
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 20)
        self.score = score
        self.score_img = self.font.render(f'Кораблей потоплено: {str(self.score)}', True, (0, 0, 0))

    def update(self):
        self.score += 1
        self.score_img = self.font.render(f'Кораблей потоплено: {str(self.score)}', True, (0, 0, 0))

    def draw_score(self):
        self.screen.blit(self.score_img, (self.screen.get_rect().width - self.score_img.get_rect().width - 10, 10))
