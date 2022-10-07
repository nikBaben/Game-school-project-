from styles import back_ground

class Back():
    def __init__(self, screen):
        self.screen = screen
        self.image = back_ground.convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
       
    def output_back(self):
        self.screen.blit(self.image, self.rect)
