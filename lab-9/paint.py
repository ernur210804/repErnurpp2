import math

import pygame
import os

pygame.init() #init
running = True

PLUS=pygame.transform.scale(pygame.image.load(os.path.join('Assets','plus.png')),(10,10))
MINUS=pygame.transform.scale(pygame.image.load(os.path.join('Assets','minus.png')),(10,10))

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1000, 600) #window size
RED = (255, 0, 0) #colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = pygame.Color('orange')
INDIGO = pygame.Color('indigo')
PURPLE = pygame.Color('purple')

screen = pygame.display.set_mode(WINDOW_SIZE)   #window

color = BLACK   # default color of shapes
color_name = 'BLACK'
shape = 'line'  # mode, which shae to draw

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('uPaint')  # name of window
screen.fill(WHITE)

prev, cur = None, None  # current and previous points
width = 1

color_index = (RED,WHITE,GREEN,BLUE,BLACK,ORANGE,INDIGO,PURPLE)
color_index_name = ('RED','WHITE','GREEN','BLUE','BLACK','ORANGE','INDIGO','PURPLE')
n=7


shape_index = ('circle','rectangle','line','eraser','square','equilateral_triangle','right_triangle','rhombus')
i=2

font = pygame.font.SysFont('Verdana', 15)  # font

pygame.draw.line(screen, pygame.Color('purple'), (0, 31), (WINDOW_WIDTH, 31), 5)   # splitting line

while running:
    pos=pygame.mouse.get_pos()
    print(pos)
   # print(pos)
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 30))  # updating status
    screen.blit(font.render(f'Mode: {shape}', True, BLACK), (10, 10))  # current shape
    screen.blit(font.render(f'Width: {width}', True, BLACK), (310, 10))  # current width
    screen.blit(font.render(f'Color:{color_index_name[n]}', True, BLACK), (610, 10))  # current color
    screen.blit(MINUS,(590,18))
    screen.blit(PLUS,(800,18))
    screen.blit(PLUS,(380,18))
    screen.blit(MINUS,(295,18))
    screen.blit(PLUS,(200,18))
    
    #pygame.draw.rect(screen,BLACK,[590,18,10,10])#switcher
    #pygame.draw.rect(screen,BLACK,[800,18,10,10])
    #pygame.draw.rect(screen,BLACK,[380,18,10,10])
    #pygame.draw.rect(screen,BLACK,[295,18,10,10])
    #pygame.draw.rect(screen,BLACK,[100,18,10,10])
    
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]  # press ctrl
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]  # press alt

        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            if 15 <= pygame.mouse.get_pos()[1] <= 25 and 550 <= pygame.mouse.get_pos()[0] <= 610:
                if n<=-1:
                    n=7
                n -=1
                color = color_index[n]
            
            if 15 <= pygame.mouse.get_pos()[1] <= 25 and 790 <= pygame.mouse.get_pos()[0] <= 810:
                if n>=7:
                    n=0
                n +=1
                color = color_index[n]
                
            if 15 <= pygame.mouse.get_pos()[1] <= 25 and 370 <= pygame.mouse.get_pos()[0] <= 390:
               
                width +=1
            
            if 15 <= pygame.mouse.get_pos()[1] <= 25 and 295 <= pygame.mouse.get_pos()[0] <= 315:
               
                width -=1
                if width <=0:
                    width =1
            
            if 15 <= pygame.mouse.get_pos()[1] <= 25 and 190 <= pygame.mouse.get_pos()[0] <= 210:
                i -= 1               
                if i<=-1:
                   i=7
                shape = shape_index[i]
                
                
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:  # change width
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if alt_pressed and pressed[pygame.K_b]:  # change color
                color = BLUE
                color_name = "BLUE"
            if alt_pressed and pressed[pygame.K_r]:
                color = RED
                color_name = 'RED'
            if alt_pressed and pressed[pygame.K_g]:
                color = GREEN
                color_name = 'GREEN'    
            if alt_pressed and pressed[pygame.K_p]:
                color = pygame.Color('purple')
                color_name = 'PURPLE'
            if alt_pressed and pressed[pygame.K_o]:
                color = pygame.Color('orange')
                color_name = 'ORANGE'
            if alt_pressed and pressed[pygame.K_i]:
                color = pygame.Color('indigo')
                color_name = 'INDIGO'
            if ctrl_pressed and pressed[pygame.K_c]:  # change shape
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_s]:
                shape = 'square'
            if ctrl_pressed and pressed[pygame.K_t]:
                shape = 'equilateral_triangle'
            if ctrl_pressed and pressed[pygame.K_m]:
                shape = 'right_triangle'
            if ctrl_pressed and pressed[pygame.K_h]:
                shape = 'rhombus'
        if shape == 'line' or shape == 'eraser':  # line and erasor have approximate same algorithm
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, WHITE, prev, cur, width)  # key word is white
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()  # if I press button I get previous point
            if event.type == pygame.MOUSEBUTTONUP:
                cur = pygame.mouse.get_pos()   # if I stop pressing the button I get current point
                if shape == 'circle':
                    x = (prev[0]+cur[0])/2  # coordinates of center
                    y = (prev[1]+cur[1])/2
                    rx = abs(prev[0]-cur[0])/2  # radius by Ox and Oy
                    ry = abs(prev[1]-cur[1])/2
                    r = (rx + ry)/2  # radius
                    pygame.draw.circle(screen, color, (x, y), r, width)
                elif shape == 'rectangle' or shape == 'square':
                    x = min(prev[0], cur[0])  #minimal coordinate
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  # length
                    ly = abs(prev[1]-cur[1])
                    if shape == 'square':
                        lx = (lx+ly)/2  # length and width are same for square
                        ly = lx
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
                elif shape == 'right_triangle' or shape == 'equilateral_triangle':
                    x = min(prev[0], cur[0])  #minimal coordinate
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  # length of pseudo rectangle
                    ly = abs(prev[1]-cur[1])
                    if shape == 'right_triangle':
                        ly = math.sqrt(lx**2 - (lx/2)**2)  # all sides are equal
                    points = (x, y+ly), (x+lx/2, y), (x+lx, y+ly)  # draw by three points
                    pygame.draw.polygon(screen, color, points, width)
                elif shape == 'rhombus':
                    x = min(prev[0], cur[0])  # minimal coordinates
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  #sizes
                    ly = abs(prev[1]-cur[1])
                    points = (x+lx/2, y), (x+lx, y+ly/2), (x+lx/2, y+ly), (x, y+ly/2)
                    pygame.draw.polygon(screen, color, points, width)  # draw by points
    pygame.display.flip()  #updating te screen
    clock.tick(fps)

pygame.quit()