import pygame as pg
from random import randrange
import random


class food: #Class for food
    def _init_(self): #random food spawnpoint
        self.rectx = int(random.randint(0, WINDOW)/ TILE_SIZE) * TILE_SIZE
        self.recty = int(random.randint(0, WINDOW)/ TILE_SIZE) * TILE_SIZE
        self.rect = pygame.Rect(self.rectx, self.recty, TILE_SIZE, TILE_SIZE)


class powerApple(food): #arv
    def _init_(self):
        segments = [snake.copy()*2]



WINDOW = 1000 #window size
TILE_SIZE = 40 #Tile sizes on the screen
RANGE = (TILE_SIZE // 4, WINDOW - TILE_SIZE // 4, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)] #function for position
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2]) #Properties for snake
snake.center = get_random_position() #random spawnpoint for snake
length = 1 #For snake lenght
segments = [snake.copy()] #Creates a copy of snace Rect
snake_dir = (0, 0) #start direction
time, time_step = 0, 110
food = snake.copy() #action when food coolid with snake
food.center = get_random_position() #food random spawnpoint
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock() #time for framerate
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN: #When w,a,s,d gets pressed, change direction
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1} #dirs = Set opposite key to 0, unavailable to self eat
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
    screen.fill('black')

    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1 #if snake touches segment
    if snake.left < 0  or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating: #if snake touches borders
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]

    if snake.center == food.center: #if food get touched, get new rand position + add lenght to snake
        food.center = get_random_position()
        length += 1
    pg.draw.rect(screen, 'red', food)
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    time_now = pg.time.get_ticks()

    if time_now - time > time_step: # if game restart, remove
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pg.display.flip()
    clock.tick(60) #60 framerate
