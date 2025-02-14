from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.side = 10
        self.shot = False
        self.hp = 360
        self.rect = pygame.Rect(*player_pos, self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def check_wall(self, x, y, mini_map):
        return (x // TILE * MAP_TILE, y // TILE * MAP_TILE) not in mini_map

    def check_wall_collision(self, dx, dy, mini_map):
        if self.check_wall(int(self.x + dx), int(self.y), mini_map):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy), mini_map):
            self.y += dy

    def movement(self, walls, mini_map):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            self.check_wall_collision(dx, dy, mini_map)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.check_wall_collision(dx, dy, mini_map)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.check_wall_collision(dx, dy, mini_map)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.check_wall_collision(dx, dy, mini_map)
        self.angle %= pi_2

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY

    def update(self, walls, mini_map):
        self.movement(walls, mini_map)
        self.mouse_control()
