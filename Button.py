import pygame
from settings import *

pygame.init()


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x * WIDTH
        self.y = y * HEIGHT
        self.width = width * WIDTH
        self.height = height * HEIGHT
        self.surf = pygame.Surface((self.width, self.height))
        self.text = text
        self.render = pygame.font.SysFont('arial', 40).render(text, False, green)
        self.surf.fill(white)
        self.render_pos = (25, 5)
        self.surf.blit(self.render, self.render_pos)
        self.beated = 0

    def is_hover(self):
        mx, my = pygame.mouse.get_pos()
        if self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height:
            return True
        return False

    def is_clicked(self):
        if self.is_hover() and pygame.mouse.get_pressed()[0]:
            return True
        return False

    def fill_green(self):
        self.surf.fill(dark_green)
        self.surf.blit(self.render, self.render_pos)
