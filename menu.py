import pygame
from Button import Button
from settings import *

pygame.init()


class Menu:
    def __init__(self, screen,buttons):
        self.screen = screen
        self.buttons = buttons

    def draw(self):
        for button in self.buttons:
            if button.beated:
                button.surf.fill(dark_green)
                button.surf.blit(button.render, button.render_pos)
                self.screen.blit(button.surf, (button.x, button.y))
                continue
            button.surf.fill(grey)
            button.surf.blit(button.render, button.render_pos)
            if button.is_hover():
                button.surf.fill(light_grey)
                button.surf.blit(button.render,button.render_pos)
            if button.is_clicked():
                button.surf.fill(dark_green)
                button.surf.blit(button.render,button.render_pos)
            self.screen.blit(button.surf,(button.x,button.y))
