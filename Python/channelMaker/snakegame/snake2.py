import pygame
from pygame.math import Vector2
import random
import array


#public cycle = [[143,144,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10],
#                    [142,133,132,123,122, 17, 16, 15, 14, 13, 12, 11],
#                    [141,134,131,124,121, 18, 19, 20, 21, 22, 23, 24],
#                    [140,135,130,125,120,115,114,109,108, 35, 34, 25],
#                    [139,136,129,126,119,116,113,110,107, 36, 33, 26],
#                    [138,137,128,127,118,117,112,111,106, 37, 32, 27],
#                    [ 85, 86, 87, 88, 89, 90, 91, 92,105, 38, 31, 28],
#                    [ 84, 83, 80, 97, 96, 95, 94, 93,104, 39, 30, 29],
#                    [ 79, 80, 81, 98, 99,100,101,102,103, 40, 45, 46],
#                    [ 78, 67, 66, 65, 64, 63, 62, 61, 60, 41, 44, 47],
#                    [ 77, 68, 69, 70, 71, 56, 57, 58, 59, 42, 43, 48],
#                    [ 76, 75, 74, 73, 72, 55, 54, 53, 52, 51, 50, 49]]
#
#def hamiltonian_path():
#    xpos = 2
#    ypos = 0
#    path_num = 1
#    if path_num + 1 == cycle[xpos + 1][ypos]:
#        direction = right
#        xpos = xpos + 1
#    if path_num + 1 == cycle[xpos][ypos + 1]:
#        direction = down
#        ypos = ypos + 1
#    if path_num + 1 == cycle[xpos - 1][ypos]:
#        direction = left
#        xpos = xpos - 1
#    if path_num + 1 == cycle[xpos][ypos - 1]:
#        direction = up
#        ypos = ypos - 1


class SNAKE:
    def __init__(self):
        self.body = [Vector2(2,0), Vector2(1,0),Vector2(0,0)]
        self.direction = Vector2(1,0)
        self.growing = False

    def move(self):
        if self.growing == False:
            self.body_copy = self.body[:-1]
            self.body_copy.insert(0, self.body[0] + self.direction)
            self.body = self.body_copy
        elif self.growing == True:
            self.body_copy = self.body[:]
            self.body_copy.insert(0, self.body[0] + self.direction)
            self.body = self.body_copy
            self.growing = False

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x*cell_size), int(block.y*cell_size), cell_size, cell_size)
            pygame.draw.rect(screen,(0,255,0),snake_rect)

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_num)
        self.y = random.randint(0, cell_num)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.cycle =((143,144,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10),
                    (142,133,132,123,122, 17, 16, 15, 14, 13, 12, 11),
                    (141,134,131,124,121, 18, 19, 20, 21, 22, 23, 24),
                    (140,135,130,125,120,115,114,109,108, 35, 34, 25),
                    (139,136,129,126,119,116,113,110,107, 36, 33, 26),
                    (138,137,128,127,118,117,112,111,106, 37, 32, 27),
                    ( 85, 86, 87, 88, 89, 90, 91, 92,105, 38, 31, 28),
                    ( 84, 83, 80, 97, 96, 95, 94, 93,104, 39, 30, 29),
                    ( 79, 80, 81, 98, 99,100,101,102,103, 40, 45, 46),
                    ( 78, 67, 66, 65, 64, 63, 62, 61, 60, 41, 44, 47),
                    ( 77, 68, 69, 70, 71, 56, 57, 58, 59, 42, 43, 48),
                    ( 76, 75, 74, 73, 72, 55, 54, 53, 52, 51, 50, 49))

        self.xpos = 2
        self.ypos = 0
        self.path_num = 1

    def update(self):
        self.hamiltonian_path()
        self.snake.move()
        self.snake_grow()
        self.check_fail()
        self.check_overlap()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_fail(self):
        if not cell_num > self.snake.body[0].x >= 0 or not cell_num > self.snake.body[0].y >= 0:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        print("The snake has died")
        pygame.quit()

    def snake_grow(self):
        if self.snake.body[0] == self.fruit.pos:
            self.snake.growing = True
            self.fruit.randomize()

    def check_overlap(self):
        for block in self.snake.body[:]:
            if self.fruit.pos == block:
                self.fruit.randomize()

    def hamiltonian_path(self):
        if int(self.path_num + 1) == int(self.cycle[self.xpos + 1][self.ypos]):
            self.snake.direction = Vector2(1,0)
            self.xpos = self.xpos + 1
            self.path_num = self.path_num + 1
            print(self.path_num)
            print("right")
        if int(self.path_num + 1) == int(self.cycle[self.xpos][self.ypos + 1]):
            self.snake.direction = Vector2(0,1)
            self.ypos = self.ypos + 1
            self.path_num = self.path_num + 1
            print("down")
        if int(self.path_num + 1) == int(self.cycle[self.xpos - 1][self.ypos]):
            self.snake.direction = Vector2(-1,0)
            self.xpos = self.xpos - 1
            self.path_num = self.path_num + 1
            print("left")
        if int(self.path_num + 1) == int(self.cycle[self.xpos][self.ypos - 1]):
            self.snake.direction = Vector2(0,-1)
            self.ypos = self.ypos - 1
            self.path_num = self.path_num + 1
            print("up")
        else:
            print("yo mama gae")

        #def hamiltonian_path(self):
        #if self.xpos + 1 < len(self.cycle) and int(self.path_num + 1) == int(self.cycle[self.xpos + 1][self.ypos]):
        #    self.snake.direction = Vector2(1,0)
        #    self.xpos = self.xpos + 1
        #    self.path_num = self.path_num + 1
        #    print(self.path_num)
        #    print("1")
        #elif self.ypos + 1 < len(self.cycle[0]) and int(self.path_num + 1) == int(self.cycle[self.xpos][self.ypos + 1]):
        #    self.snake.direction = Vector2(0,1)
        #    self.ypos = self.ypos + 1
        #    self.path_num = self.path_num + 1
        #    print("2")
        #elif self.xpos - 1 >= int(0) and int(self.path_num + 1) == int(self.cycle[self.xpos - 1][self.ypos]):
        #    self.snake.direction = Vector2(-1,0)
        #    self.xpos = self.xpos - 1
        #    self.path_num = self.path_num + 1
        #    print("3")
        #elif self.ypos - 1 >= int(0) and int(self.path_num + 1) == int(self.cycle[self.xpos][self.ypos - 1]):
        #    self.snake.direction = Vector2(0,-1)
        #    self.ypos = self.ypos - 1
        #    self.path_num = self.path_num + 1
        #    print("4")
        #else:
        #    print("yo mama gae")

pygame.init()

cell_num = 12
cell_size = 40

left = Vector2(-1,0)
right = Vector2(1,0)
up = Vector2(0,-1)
down = Vector2(0,1)

screen = pygame.display.set_mode((cell_num*cell_size, cell_num*cell_size))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)

main = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = up
            if event.key==pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = down
            if event.key==pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = right
            if event.key==pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = left

    main.draw_elements()
    screen.fill((0,0,0))
    main.draw_elements()
    pygame.display.update()
    #clock.tick(60)
