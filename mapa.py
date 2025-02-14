from settings import *
import pygame

text_map1 = ['############',
             '#.....##...#',
             '#..##....###',
             '#.....##...#',
             '##.....#...#',
             '#..#...#...#',
             '#..##......#',
             '############', ]

text_map2 = ['############',
             '#...####...#',
             '###......#.#',
             '###......#.#',
             '##.....#...#',
             '#......#...#',
             '##.##..#...#',
             '############', ]
world_map = {}
mini_map = set()
walls = []

for j, row in enumerate(text_map1):
    for i, char in enumerate(row):
        if char == '#':
            world_map[(i * TILE, j * TILE)] = '#'
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
levels = [[world_map, mini_map, walls]]

world_map = {}
mini_map = set()
walls = []

for j, row in enumerate(text_map2):
    for i, char in enumerate(row):
        if char == '#':
            world_map[(i * TILE, j * TILE)] = '#'
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
levels.append([world_map, mini_map, walls])