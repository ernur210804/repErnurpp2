import pygame
import sys
from pygame.locals import *
import random
import time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

YELLOW = (255, 191, 0)
BLUE = (0, 30, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
SCORE2 = 0

font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(os.path.join("Assets","street.png"))
background = pygame.transform.scale(background, (600, 800))

Display = pygame.display.set_mode((600, 800))
Display.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(os.path.join("Assets","red-car.png"))
        
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        
        if (self.rect.top > 800 ):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(os.path.join("Assets","purple-car.png"))
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        
        if (self.rect.top > 800):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)




class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("Assets","coin.png"))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("Assets","green-car.png"))
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()


        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
E2 = Enemy2()
C1 = Point()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Display.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    Display.blit(scores, (10, 10))
    scores2 = font_small.render('Coins:' + str(SCORE2), True, YELLOW)
    Display.blit(scores2, (SCREEN_WIDTH-130, 10))

    for entity in all_sprites:
        Display.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        sound = pygame.mixer.Sound('crash.wav')
        sound.set_volume(0.02)
        sound.play()
        time.sleep(0.5)

        Display.fill(BLACK)
        f = pygame.font.Font(None, 80)
        scores = f.render('Game over', True, RED)
        Display.blit(scores, (50, 275))
        #Display.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, coins):
        C1.rect.top = 0
        C1.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
        SCORE2 += 1
       
    pygame.display.update()
    FramePerSec.tick(FPS)