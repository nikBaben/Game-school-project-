import pygame

NON_ACTIVE = (0, 0, 0)
ACTIVE = (255, 255, 255)
class MenuItem():
    def __init__(self, text, func, item_pos):
        self.font = pygame.font.SysFont(None, 40, True)
        self.text = text
        self.action = func
        self.color = NON_ACTIVE
        self.text_img = self.font.render(self.text, True, self.color)
        self.x, self.y = item_pos

    def check_hover(self, pos):
        x, y = pos
        return (self.x <= x <= self.x + self.text_img.get_width()) and (
                    self.y <= y <= self.y + self.text_img.get_height())
    def draw_item(self, screen):
        screen.blit(self.text_img, (self.x, self.y))


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.items = []
        self.cur_x = self.screen.get_width() // 2
        self.cur_y= 400

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.cur_y += 30


    def update(self, pos):
        for item in self.items:
            if item.check_hover(pos):
                item.color = ACTIVE
            else:
                item.color = NON_ACTIVE
            item.text_img = item.font.render(item.text, True, item.color)

    def check_click(self, pos):
        for item in self.items:
            if item.check_hover(pos):
                item.action()

    def draw(self):
        for item in self.items:
            item.draw_item(self.screen)

