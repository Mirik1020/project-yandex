import pygame
from settings import *
from ray_casting import ray_casting
from collections import deque


class Drawing:
    def __init__(self, screen, map_screen, player):
        self.screen = screen
        self.map_screen = map_screen
        self.player = player
        self.font = pygame.font.SysFont('Arial', 30, bold=True)
        self.textures = {
            'S': pygame.image.load('img/sky.png')
        }
        self.weapon_base_sprite = pygame.image.load('base/0.png').convert_alpha()
        self.weapon_shot_animation = deque([pygame.image.load(f'shot/{i}.png').convert_alpha()
                                            for i in range(20)])
        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 2, HEIGHT - self.weapon_rect.height)
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_speed = 1
        self.shot_animation_count = 0
        self.shot_animation_trigger = True

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, grey, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda x: x[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)

        # ray_casting(player_pos, player_angle)

    def show_fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, red)
        self.screen.blit(render, FPS_POS)

    def mini_map(self, player, mini_map):
        self.map_screen.fill(black)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.map_screen, green, (map_x, map_y),
                         (map_x + d * math.cos(player.angle), map_y + d * math.sin(player.angle)))
        pygame.draw.circle(self.map_screen, green, (map_x, map_y), 3)

        for x, y in mini_map:
            pygame.draw.rect(self.map_screen, dark_green, (x, y, MAP_TILE, MAP_TILE))

        self.screen.blit(self.map_screen, MAP_POS)

    def weapon(self):
        if self.player.shot:
            shot_sprite = self.weapon_shot_animation[self.shot_length_count]
            self.screen.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            if self.shot_animation_count == self.shot_animation_speed:
                self.shot_animation_count = 0
                self.shot_length_count += 1
                self.shot_animation_trigger = False
            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.shot_animation_trigger = True
        else:
            self.screen.blit(self.weapon_base_sprite, self.weapon_pos)

    def health_bar(self):
        surf1 = pygame.Surface((200, 50))
        surf1.fill(dark_grey)

        surf2 = pygame.Surface((100, 20))
        surf2.fill(red)

        surf3 = pygame.Surface((100 * self.player.hp // 360, 20))
        surf3.fill(green)

        surf2.blit(surf3, (0, 0))
        surf1.blit(surf2, (200 // 2 - 100 // 2, 50 // 2 - 20 // 2))
        self.screen.blit(surf1, (WIDTH - 300, HEIGHT - 50))
