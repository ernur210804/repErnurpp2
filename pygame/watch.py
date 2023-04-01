import pygame
from math import pi,sin,cos
import datetime
import os

WIDTH,HEIGHT=800,800
center=(WIDTH/2,HEIGHT/2)
clock_radius=400

pygame.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CLOCK")
clock=pygame.time.Clock()
FPS=60

mickey_clock=pygame.image.load(os.path.join('Assets','mickeyclock.jpeg'))
mickey_clock=pygame.transform.scale(mickey_clock,(800,800))

mickey_min=pygame.image.load(os.path.join('Assets','minhand.png'))
mickey_min=pygame.transform.scale(mickey_min,(500,80))
mickey_min_rect=mickey_min.get_rect()
mickey_min_rect.center=(400,400)

mickey_sec=pygame.image.load(os.path.join('Assets','sechand.png'))
mickey_sec=pygame.transform.scale(mickey_sec,(500,70))
mickey_sec_rect=mickey_sec.get_rect()
mickey_sec_rect.center=(400,400)

        

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
   

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                
        current_time=datetime.datetime.now()
        second=current_time.second
        minute=current_time.minute
        hour=current_time.hour
        

        
        screen.fill(BLACK)
        pygame.draw.circle(screen,WHITE,center,clock_radius-10,10)
        pygame.draw.circle(screen,WHITE,center,12)
        
        screen.blit(mickey_clock,(0,0))
        
        
        
        rot_mickey_min=pygame.transform.rotate(mickey_min,( -1 * (6 * minute) - 160))
        rot_mickey_min_rect=rot_mickey_min.get_rect()
        rot_mickey_min_rect.center=mickey_min_rect.center
        screen.blit(rot_mickey_min,rot_mickey_min_rect)
        
        rot_mickey_sec=pygame.transform.rotate(mickey_sec,(-1*(6*second)+90))
        rot_mickey_sec_rect=rot_mickey_sec.get_rect()
        rot_mickey_sec_rect.center=mickey_sec_rect.center
        screen.blit(rot_mickey_sec,rot_mickey_sec_rect)
        
        
        
        
        
        pygame.display.update()
        
        clock.tick(FPS)
    pygame.quit()

main()
                

