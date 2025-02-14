import pygame
from settings import *


class EndScreen:
    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.render = pygame.font.SysFont('arial', 60).render(self.text, False, green)
        self.render_pos = (100, 0)

    def draw(self):
        self.screen.fill(black)
        self.screen.blit(self.render, self.render_pos)

    def set_text(self,text):
        self.render = pygame.font.SysFont('arial', 60).render(text, False, green)
        self.screen.fill(black)
        self.screen.blit(self.render, self.render_pos)
