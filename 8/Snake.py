import pygame
import time
import random

pygame.init()
# Parameters of Display
WIDTH, HEIGHT = 1200, 900
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game parameters
FPS = 10 
RUN = True
SCORE = 0
LEVEL = 1
level_added = False
fruit_spawn = True
black = (0,0,0)
red = (255,0,0)
# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.snake_position = [210, 60]  # START point
        self.snake_body = [[210, 60], [180, 60], [150, 60], [120, 60]]  # Body coordinate and 30x30 one body part
        self.snake_color = (108, 187, 60)
        self.size_x, self.size_y = 30, 30

    def move(self, direction):
        if direction == "UP":
            self.snake_position[1] -= self.size_y
        if direction == "DOWN":
            self.snake_position[1] += self.size_y
        if direction == "LEFT":
            self.snake_position[0] -= self.size_x
        if direction == "RIGHT":
            self.snake_position[0] += self.size_x

    def grow(self):
        self.snake_body.insert(0, list(self.snake_position))

    def shrink(self):
        self.snake_body.pop()

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fruit_position = [random.randrange(0, (WIDTH // 30)) * 30, random.randrange(0, (HEIGHT // 30)) * 30]  # fruit position

    def update(self):
        self.fruit_position = [random.randrange(0, (WIDTH // 30)) * 30, random.randrange(0, (HEIGHT // 30)) * 30]

S = Snake()
F = Fruit()

def draw_grid():
    for x in range(0, WIDTH, 30): # 0 - 1200 divided by 30 
        pygame.draw.line(surface, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 30):# 0 - 900 divided by 30 
        pygame.draw.line(surface, (200, 200, 200), (0, y), (WIDTH, y))

def show_score(color, font, size):
    #creating font and level
    score_font = pygame.font.SysFont(font,size)
    level_font = pygame.font.SysFont(font,size)
    # create the display surface object
    score_surface = score_font.render("Score : " + str(SCORE), True , color) # antialias - сглаживание  true
    level_surface = level_font.render("Level : " + str(LEVEL), True , color) #string
    # create a rectangular object for the text
    score_rect = score_surface.get_rect()
    score_rect.x , score_rect.y = 0 , 0
    level_rect = level_surface.get_rect()
    level_rect.x , level_rect.y = 0 , 30
    surface.blit(score_surface ,score_rect)
    surface.blit(level_surface ,level_rect) #(what show, which size)


while RUN:
    tickrate = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        # parameters for move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"

    # Here we check if snake moving right, snake cannot move left
    if direction != "UP" and change_to == "DOWN":
        direction = "DOWN"
    if direction != "DOWN" and change_to == "UP":
        direction = "UP"
    if direction != "LEFT" and change_to == "RIGHT":
        direction = "RIGHT"
    if direction != "RIGHT" and change_to == "LEFT":
        direction = "LEFT"

    S.move(direction)

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 1
    S.grow()  # insert add in 0 position in list and add from head
    
    if S.snake_position[0] == F.fruit_position[0] and S.snake_position[1] == F.fruit_position[1]:
        SCORE += 1
        fruit_spawn = False
    else:
        S.shrink()  # deleted last rectangle
    #how this work +1  and -1 if nothing special if snake ate fruit else function ignore

    if not fruit_spawn:
        F.update()
        fruit_spawn = True
    
    if SCORE % 5 == 0 and not level_added and SCORE != 0: # example 10 #next loop again 10 but here is true so added only one time
        LEVEL += 1
        FPS += 2
        level_added = True #true 
    elif SCORE % 5 != 0:
        level_added = False

    #center for x ,y circle apple
    x = F.fruit_position[0] + 15
    y = F.fruit_position[1] + 15

    surface.fill((255, 255, 255))  # white
    draw_grid()  # draw the grid
    for pos in S.snake_body:
        pygame.draw.rect(surface, (S.snake_color), pygame.Rect(pos[0], pos[1], S.size_x, S.size_y))
    pygame.draw.circle(surface, red, (x,y), 15) #radius 15
    pygame.draw.circle(surface, (255,165,0), (x-3,y-3), 7) #orange
    pygame.draw.circle(surface, (255,255,255), (x -3 ,y- 3), 5) #white

    # here we check that will snake pass the border
    if S.snake_position[0] < 0 or S.snake_position[0] > WIDTH - S.size_x:
        RUN = False
    if S.snake_position[1] < 0 or S.snake_position[1] > HEIGHT - S.size_y:
        RUN = False
    # Here we check that will snake touch itself
    for body in S.snake_body[1:]:  # without head snake
        if S.snake_position[0] == body[0] and S.snake_position[1] == body[1]:
            RUN = False

    show_score( black, 'times new roman', 30)
    pygame.display.update()
    tickrate.tick(FPS)


time.sleep(1)
pygame.quit()


