import pygame, sys
from pygame.locals import*
import random, time

pygame.init()
FPS=60
FramePerSec=pygame.time.Clock()

#Colors
BLUE=(0, 0, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)

#Setting for screen and game
SCREEN_WIDTH=400
SCREEN_HEIGHT=600
SPEED=5
SCORE=0
COINS_COUNT=0
COINS_FOR_SPEED=10

#Font for game
font=pygame.font.SysFont("Verdana", 60)
font_smaller=pygame.font.SysFont("Verdana", 20)
game_over=font.render("Game Over", True, BLACK)

#Background for game
background=pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\AnimatedStreet.png")

#Creating a screen
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer game")

#Class of enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top>600:
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(40, SCREEN_WIDTH-40), 0)

#Class of player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160, 520)
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left>0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right<SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top>0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom<SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

#Class of coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH-40), random.randint(50, 300))
    def move(self):
        if self.rect.top>600:
            self.rect.top=random.randint(50, 300)
            self.rect.center=(random.randint(40, SCREEN_WIDTH-40), self.rect.top)


#Creating a sprites
P1=Player()
E1=Enemy()
C1=Coin()

enemies=pygame.sprite.Group()
enemies.add(E1)

coins=pygame.sprite.Group()
coins.add(C1)

all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Event for increasing of speed
INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 1000)

#Game cycle
while True:
    for event in pygame.event.get():
        if event.type==INC_SPEED:
            SPEED+=0.5
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    #Painting background
    screen.blit(background, (0,0))

    #Rendering scores
    score_text=font_smaller.render(f"Score:{SCORE}", True, BLACK)
    screen.blit(score_text, (0,0))
    coint_collected_text=font_smaller.render(f"Coins:{COINS_COUNT}", True, BLACK)
    screen.blit(coint_collected_text, (SCREEN_WIDTH-120, 10))

    #Moving and painting objects
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    #Checking for crashes with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    #Checking for interaction with coins
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COUNT+=random.randint(1, 3)
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))
        if COINS_COUNT%COINS_FOR_SPEED==0:
            SPEED+=1
    
    pygame.display.update()
    FramePerSec.tick(FPS)