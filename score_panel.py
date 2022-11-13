import pygame


class Score_panel():
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 20)
        self.record = score
        self.new_score = 0
        self.record_img = self.font.render(f'Ваш рекорд: {str(self.record)}', True, (0, 0, 0))
        self.new_score_img = self.font.render(f'Кораблей потоплено: {str(self.new_score)}', True, (0, 0, 0))

    def update(self):
        self.new_score += 1
        self.new_score_img = self.font.render(f'Кораблей потоплено: {str(self.new_score)}', True, (0, 0, 0))

    def draw_score(self):
        self.screen.blit(self.record_img, (self.screen.get_rect().width - self.record_img.get_rect().width - 10, 10))
        self.screen.blit(self.new_score_img, (self.screen.get_rect().width - self.new_score_img.get_rect().width - 10, 30))