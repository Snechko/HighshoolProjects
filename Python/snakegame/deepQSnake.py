import pygame, sys
from pygame.math import Vector2
import random


class SNAKE:
    def __init__(self):
        self.body = [Vector2(3,1),Vector2(2,1),Vector2(1,1)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x*cell_size), int(block.y*cell_size), cell_size, cell_size)
            pygame.draw.rect(screen,(0,255,0), block_rect)
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body= body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body= body_copy[:]

    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect) 

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):

        self.snake.move_snake()
        self.chack_collision()
        self.check_fail()

        self.fruit_overlap()


            
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def chack_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not cell_number > self.snake.body[0].x >= 0 or not cell_number > self.snake.body[0].y >= 0:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def fruit_overlap(self):
        for block in self.snake.body:
            if block == self.snake.body[:]:
                self.fruit.randomize()




pygame.init()
cell_size = 40
cell_number = 16
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()



main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction=Vector2(1,0)
            if event.key==pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction=Vector2(-1,0)
            

    screen.fill((0,0,0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
