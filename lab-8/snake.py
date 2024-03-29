import pygame, random, sys ,os,time
from pygame.locals import *

snake_speed = 10

class Constant:
    window_x = 720
    window_y = 480

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


pygame.init()

pygame.display.set_caption('Snakee')
game_window = pygame.display.set_mode((Constant.window_x, Constant.window_y))


FPS = pygame.time.Clock()

snake_position = [100, 50]

# определение первых 4 блоков тела змеи
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (Constant.window_x // 10)) * 10,
                  random.randrange(1, (Constant.window_y // 10)) * 10]

fruit_position2 = [random.randrange(1, (Constant.window_x // 10)) * 10,
                  random.randrange(1, (Constant.window_y // 10)) * 10]

fruit_spawn = True
fruit_spawn2 = True


# право
direction = 'RIGHT'
change_to = direction

# начальная оценка
score = 0
level = 0
x = 0


# отображение функции Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)


    score_surface = score_font.render('Score : ' + str(score), True, color)

  
    score_rect = score_surface.get_rect()

   
    game_window.blit(score_surface, score_rect)


def show_level(choice, color, font, size):
    # создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

   
    score_surface = score_font.render('Level : ' + str(level), True, color)

    
    score_rect = score_surface.get_rect(topright=(650, 0))

    
    game_window.blit(score_surface, score_rect)



def game_over():
   
    my_font = pygame.font.SysFont('arial', 50)

   
    game_over_surface = my_font.render(
        'Score is : ' + str(score) + '  Level :' + str(level), True, Constant.red)

   
    game_over_rect = game_over_surface.get_rect()

   
    game_over_rect.midtop = (Constant.window_x / 2, Constant.window_y / 4)

    
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

   
    time.sleep(3)

    
    pygame.quit()

   
    quit()




tm = time.time()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    
    if direction == 'UP':
        snake_position[1] -= 10
        
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Механизм роста тела змеи
    # если фрукты и змеи сталкиваются, то очки
    # будет увеличено на 10
    snake_body.insert(0, list(snake_position))
    if (snake_position[0] == fruit_position[0] or snake_position[0]== fruit_position2[0]) and (snake_position[1] == fruit_position[1] or snake_position[1] == fruit_position2[1]):
        score += random.randrange(10, 31, 10)
        fruit_spawn = False
        
    else:
        # timer and change pos
        if time.time() - tm > 5:
            tm = time.time()
            fruit_spawn = False
            
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (Constant.window_x // 10)) * 10,
                          random.randrange(1, (Constant.window_y // 10)) * 10]
        fruit_position2 = [random.randrange(1, (Constant.window_x // 10)) * 10,
                          random.randrange(1, (Constant.window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(Constant.black)

    if score == x + 40:
        snake_speed += 5
        level += 1
        x += 40

    for pos in snake_body:
        pygame.draw.rect(game_window, Constant.red,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, Constant.white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    pygame.draw.rect(game_window, Constant.white, pygame.Rect(
        fruit_position2[0], fruit_position2[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > Constant.window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > Constant.window_y - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score countinuously
    show_score(1, Constant.white, 'times new roman', 20)
    show_level(1, Constant.white, 'times new roman', 20)

    pygame.display.update()
    FPS.tick(snake_speed)