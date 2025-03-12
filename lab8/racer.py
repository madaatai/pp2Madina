import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Game settings
fps = 60
FramePerSec = pygame.time.Clock()

# Define colors
Blue = (0,0,255)
Red = (255,0,0)
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)

# Screen dimensions
Screen_width = 400
Screen_heigth = 600
Speed = 5
Score = 0
Coins_count = 0

# Fonts and text
font = pygame.font.SysFont("Verdana", 60)
font_smaller = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, Black)

# Load background image
background = pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\AnimatedStreet.png")

# Create game screen
screen = pygame.display.set_mode((Screen_width, Screen_heigth))
screen.fill(White)
pygame.display.set_caption("Do not crash")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Move player within screen bounds
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < Screen_width and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < Screen_heigth and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        self.rect.clamp_ip(pygame.Rect(0, 0, Screen_width, Screen_heigth))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_width - 40), 0)
    
    def move(self):
        global Score
        self.rect.move_ip(0, Speed)
        # Reset enemy position and increase score when it goes off-screen
        if self.rect.top > Screen_heigth:
            Score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_width - 40), 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab8\\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Screen_width - 40), random.randint(50, 300))
    
    def move(self):
        pass # Coin stays stationary until collected

# Create game objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Group objects for easy management
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Event to increase speed periodically
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            Speed += 0.5 # Increase enemy speed over time
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    screen.blit(background, (0, 0))
    
    # Display score and coins collected
    score_text = font_smaller.render(f"Score: {Score}", True, Black)
    screen.blit(score_text, (0, 0))
    coins_collected_text = font_smaller.render(f"Coins: {Coins_count}", True, Black)
    screen.blit(coins_collected_text, (Screen_width - 120, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    # Check for collision with enemy (Game Over)
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        screen.fill(Red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Check for collision with coin (increase coin count)
    collected_coin = pygame.sprite.spritecollideany(P1, coins)
    if collected_coin:
        Coins_count += 1
        collected_coin.rect.center = (random.randint(40, Screen_width - 40), random.randint(50, 300))
    
    # Refresh game screen
    pygame.display.update()
    FramePerSec.tick(fps)