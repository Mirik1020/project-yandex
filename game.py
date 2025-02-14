import pygame
from settings import *
from menu import Menu
from player import Player
from sprite_object import *
from ray_casting import ray_casting
from drawing import Drawing
from Button import Button
from mapa import levels
from end_screen import EndScreen
import mapa
import time

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
map_screen = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))

sprite1 = Sprites1()
sprite2 = Sprites2()
sprites = [sprite1, sprite2]

end_screen = EndScreen(screen, 'level is complete')
lost_screen = EndScreen(screen, 'you lost')
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, map_screen, player)
menu_ = Menu(screen, [Button(0.45, 0.3, 0.1, 0.1, 'play'), Button(0.45, 0.45, 0.1, 0.1, 'exit')])
lvls_ = Menu(screen,
             [Button(0.2, 0.2, 0.1 * HEIGHT / WIDTH, 0.1, 'lvl1'), Button(0.3, 0.2, 0.1 * HEIGHT / WIDTH, 0.1, 'lvl2')])
play = True
game = False
menu = True
lvls = False
end_scr = False
lost_scr = False
c = 0
st = 0
last = 0
lvl = 0
cur_sprites = sprites.copy()[lvl]
while play:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE] and lvls:
                game = False
                menu = True
                lvls = False
            elif pygame.key.get_pressed()[pygame.K_ESCAPE] and menu:
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player.shot = True
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)
    if game:
        player.update(levels[lvl][2], levels[lvl][1])
        for i in range(len(cur_sprites.list_of_objects)):
            if len(cur_sprites.list_of_objects[i].moving_arr) > 0:
                cur_sprites.list_of_objects[i].move()
            else:
                cur_sprites.list_of_objects[i].move(player.x, player.y)
        drawing.background(player.angle)
        walls = ray_casting(player, levels[lvl][0])
        locate_ = [obj.object_locate(player, walls) for obj in cur_sprites.list_of_objects]
        i = 0
        while i < len(cur_sprites.list_of_objects):
            if cur_sprites.list_of_objects[i].object_locate(player, walls)[
                0] and player.shot and drawing.shot_length_count == 2:
                cur_sprites.list_of_objects[i].hp -= 10

                if cur_sprites.list_of_objects[i].hp == 0:
                    del cur_sprites.list_of_objects[i]
                    i -= 1
            if len(cur_sprites.list_of_objects) > 0 and cur_sprites.list_of_objects[i].object_locate(player, walls)[
                0]:
                cur_sprites.list_of_objects[i].moving_arr = []
            if len(cur_sprites.list_of_objects) > 0 and ((player.x - cur_sprites.list_of_objects[i].x) ** 2 + (
                    player.y - cur_sprites.list_of_objects[i].y) ** 2) ** 0.5 < 50:
                player.hp -= 1
            i += 1
        if player.hp <= 0:
            game = False
            menu = False
            lvls = False
            lost_scr = True
            end_scr = False
            player.hp = 360
            player.x, player.y = player_pos
            player.angle = player_angle
            continue
        elif len(cur_sprites.list_of_objects) == 0:
            game = False
            menu = False
            lvls = False
            end_scr = True
            lvl += 1
            player.hp = 360
            last = time.perf_counter() - st
            continue
        drawing.world(walls + locate_)
        drawing.show_fps(clock)
        drawing.mini_map(player, levels[lvl][1])
        drawing.weapon()
        drawing.health_bar()
        pygame.mouse.set_visible(False)

    if menu:
        menu_.draw()
        for button in menu_.buttons:
            if button.is_clicked() and button.text == 'play':
                game = False
                menu = False
                lvls = True
            if button.is_clicked() and button.text == 'exit':
                exit()
        pygame.mouse.set_visible(True)
    if lvls:
        for button in lvls_.buttons:
            if button.text == 'lvl1' and lvl >= 1:
                button.beated = 1
                if button.is_clicked():
                    game = False
                    menu = False
                    lvls = False
                    end_scr = True
                continue
            if button.text == 'lvl2' and lvl >= 2:
                button.beated = 1
                if button.is_clicked():
                    game = False
                    menu = False
                    lvls = False
                    end_scr = True
                continue
            if button.is_clicked() and button.text == 'lvl1' and lvl == 0:
                game = True
                menu = False
                lvls = False
                lvl = 0
                st = time.perf_counter()
                player.x, player.y = player_pos
                cur_sprites = sprites.copy()[lvl]
                break
            elif button.is_clicked() and button.text == 'lvl2' and lvl == 1:
                game = True
                menu = False
                lvls = False
                lvl = 1
                player.x, player.y = player_pos
                st = time.perf_counter()
                cur_sprites = sprites.copy()[lvl]
                break
        lvls_.draw()

        pygame.mouse.set_visible(True)
    if end_scr:
        c += 1
        if c == 120:
            end_scr = False
            lvls = True
            c = 0
        end_screen.set_text(end_screen.text + f'   time:{int(last)}sec')
        end_screen.draw()
    if lost_scr:
        c += 1
        if c == 120:
            lost_scr = False
            lvls = True
            c = 0
        lost_screen.draw()
    pygame.display.flip()
    clock.tick(FPS)
