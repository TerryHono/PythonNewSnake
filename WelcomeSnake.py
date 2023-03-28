import pygame, sys
import time
import random

pygame.init()

width, height = 400, 400
play_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Le jeu du serpent")
x, y = 200, 200
delta_x, delta_y = 0, 0
body_list = [(x, y)]
food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
clock = pygame.time.Clock()
game = False
font = pygame.font.SysFont("", 25)


def snake():
    global x, y, food_y, food_x, game
    x = (x + delta_x) % width
    y = (y + delta_y) % height
    if (x, y) in body_list:
        game = True
        return

    body_list.append((x, y))
    if food_x == x and food_y == y:
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
    else:
        del body_list[0]

    play_screen.fill((0, 0, 0))
    score = font.render("SCORE: " + str(len(body_list)), True, (255, 255, 0))
    play_screen.blit(score, [0, 0])
    pygame.draw.rect(play_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for (i, j) in body_list:
        pygame.draw.rect(play_screen, (255, 255, 255), [i, j, 10, 10])
    pygame.display.update()


while True:
    if game:
        play_screen.fill((0, 0, 0))
        msg = font.render("Game Over!!", True, (255, 255, 255))
        play_screen.blit(msg, [width // 3, height // 3])
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
        sys.exit()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if delta_x != 10:
                    delta_x = -10
                delta_y = 0
            if event.key == pygame.K_RIGHT:
                if delta_x != -10:
                    delta_x = 10
                delta_y = 0
            if event.key == pygame.K_UP:
                if delta_y != 10:
                    delta_y = - 10
                delta_x = 0
            if event.key == pygame.K_DOWN:
                if delta_y != -10:
                    delta_y = 10
                delta_x = 0
        else:
            continue
        snake()

    if not events:
        snake()
    clock.tick(10)
