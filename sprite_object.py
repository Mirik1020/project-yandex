import pygame
from settings import *
from math import sqrt


class Sprites1:
    def __init__(self):
        self.sprite_types = {
            'devil': [pygame.image.load(f'sprites/devil/{i}.png').convert_alpha() for i in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['devil'], False, (10, 4), -0.2, 0.7, 50, [(10, 4), (10, 6), (8, 6)], 1),
            SpriteObject(self.sprite_types['devil'], False, (9.5, 1.5), -0.2, 0.7, 50, [(9.5, 1.5)], 2),
            SpriteObject(self.sprite_types['devil'], False, (1.5, 2), -0.2, 0.7, 50, [(1.5, 2), ], 3),
        ]
        self.copy_list = [
            SpriteObject(self.sprite_types['devil'], False, (10, 4), -0.2, 0.7, 50, [(10, 4), (10, 6), (8, 6)], 1),
            SpriteObject(self.sprite_types['devil'], False, (9.5, 1.5), -0.2, 0.7, 50, [(9.5, 1.5)], 2),
            SpriteObject(self.sprite_types['devil'], False, (1.5, 2), -0.2, 0.7, 50, [(1.5, 2), ], 3),
        ]


class Sprites2:
    def __init__(self):
        self.sprite_types = {
            'devil': [pygame.image.load(f'sprites/devil/{i}.png').convert_alpha() for i in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['devil'], False, (10, 4), -0.2, 0.7, 50, [(10, 4), (10, 6), (8, 6)], 1),
            SpriteObject(self.sprite_types['devil'], False, (9.5, 1.5), -0.2, 0.7, 50, [(9.5, 1.5)], 2),
        ]
        self.copy_list = [
            SpriteObject(self.sprite_types['devil'], False, (10, 4), -0.2, 0.7, 50, [(10, 4), (10, 6), (8, 6)], 1),
            SpriteObject(self.sprite_types['devil'], False, (9.5, 1.5), -0.2, 0.7, 50, [(9.5, 1.5)], 2),
        ]

class SpriteObject:
    def __init__(self, object, static, pos, shift, scale, hp, moving_arr=list(), speed=0):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale
        self.moving_arr = [(i[0] * TILE, i[1] * TILE) for i in moving_arr]
        self.speed = speed
        self.hp = hp
        self.c = 0
        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for _ in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for _ in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += pi_2

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and distance_to_sprite < fake_walls[fake_ray][0]:
            proj_height = min(int(PROJ_COOF / distance_to_sprite * self.scale), 2 * HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if theta < 0:
                    theta += pi_2
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return distance_to_sprite, sprite, sprite_pos
        else:
            return (False,)

    def move(self, x=None, y=None):
        if len(self.moving_arr) == 0 and x and y:
            x1 = x
            y1 = y
            c = sqrt((self.x - x1) ** 2 + (self.y - y1) ** 2)
            sin_a = (x1 - self.x) / c
            cos_a = (y1 - self.y) / c
            self.x += self.speed * sin_a
            self.y += self.speed * cos_a
        else:
            if abs(self.x - self.moving_arr[self.c][0]) < self.speed and abs(
                    self.y - self.moving_arr[self.c][1]) < self.speed:
                self.c += 1
                if self.c >= len(self.moving_arr):
                    self.c = 0
            x1 = self.moving_arr[self.c][0]
            y1 = self.moving_arr[self.c][1]
            c = sqrt((self.x - x1) ** 2 + (self.y - y1) ** 2)
            if (c < self.speed):
                pass
            else:
                sin_a = (x1 - self.x) / c
                cos_a = (y1 - self.y) / c
                self.x += self.speed * sin_a
                self.y += self.speed * cos_a
