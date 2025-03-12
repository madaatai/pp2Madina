import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
radius = 25
ball_x = 400 // 2
ball_y = 300 // 2
ball_color = ((255, 0, 0))
step = 20
run = True
clock = pygame.time.Clock()
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - radius - step >= 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + radius + step <= 400:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - radius - step >= 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y + radius + step <= 300:
        ball_y += step


    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), radius)

    pygame.display.flip()
    clock.tick(60)  