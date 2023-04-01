import pygame

WIDTH,HEIGHT=900,700
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
X=50
Y=50

RED=(255,0,0)


RADIUS=10

FPS=60
VEL=20

    
clock=pygame.time.Clock()

run=True
while run:
    WIN.fill((255,255,255))
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False 
       
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and X-VEL>0:#LEFT
        X-=VEL
    if keys_pressed[pygame.K_d] and X-VEL<870:#RIGHT
        X+=VEL
    if keys_pressed[pygame.K_w] and Y-VEL>0:#UP
        Y-=VEL
    if keys_pressed[pygame.K_s] and Y-VEL<670:#DOWN
        Y+=VEL
    red=pygame.draw.circle(WIN,RED,(X,Y),RADIUS)
    pygame.display.update()    
pygame.quit()
    
