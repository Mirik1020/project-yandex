import pygame
from settings import *


def ray_casting(player, world_map):
    walls = []
    player_angle = player.angle
    player_pos = player.pos
    cur_angle = player_angle - HALF_FOV
    xp, yp = player_pos
    xm, ym = mapping(xp, yp)
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - xp) / cos_a
            y = yp + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - yp) / sin_a
            x = xp + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COOF / depth

        c = 255 / (1 + depth ** 2 * 0.00002)
        color = (c // 3, c, c // 3)

        walls_column = pygame.Surface((SCALE, proj_height))
        walls_column.fill(color)
        wall_rect = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
        walls.append((depth, walls_column, wall_rect))
        cur_angle += DELTA_ANGLE
    return walls


def mapping(a, b):
    return (a // TILE * TILE, b // TILE * TILE)
