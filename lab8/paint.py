import pygame

#Intialization pygame
pygame.init()

#Parameters for window
SCREEN_WIDTH, SCREEN_HEIGHT=800, 600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

#Colors
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#Variables
running=True
drawing=False
last_pos=None
draw_mode="line"
color=BLACK
radius=5

#Paint desk
canvas=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill(WHITE)

#Game cycle
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #Checking for switching colors, and eraser
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                color=RED
            elif event.key==pygame.K_g:
                color=GREEN
            elif event.key==pygame.K_b:
                color=BLUE
            elif event.key==pygame.K_k:
                color=BLACK
            elif event.key==pygame.K_e:
                color=WHITE
                draw_mode="eraser"

        #Checking for line, circle, rectangle
        elif event.type==pygame.MOUSEBUTTONDOWN:
            last_pos=event.pos
            if event.button==1: #LBM-line
                draw_mode="line"
                drawing=True
            elif event.button==3: #RBM-rectangle
                draw_mode="rect"
            elif event.button==2: #CBM-circle
                draw_mode="circle"

        #Case when user clicked to left button of mouse
        elif event.type==pygame.MOUSEMOTION and drawing and draw_mode=="line":
            pygame.draw.line(canvas, color, last_pos, event.pos, radius)
            last_pos=event.pos

        #Case when user clicked to right button of mouse or central one       
        elif event.type==pygame.MOUSEBUTTONUP:
            if draw_mode=="rect":
                rect_x, rect_y=min(last_pos[0], event.pos[0]), min(last_pos[1], event.pos[1])
                rect_width, rect_height=abs(last_pos[0]-event.pos[0]), abs(last_pos[1]-event.pos[1])
                pygame.draw.rect(canvas, color, (rect_x, rect_y, rect_width, rect_height), radius)
            elif draw_mode=="circle":
                center_x, center_y=last_pos
                end_x, end_y = event.pos
                radius_circle = int(((end_x - center_x) ** 2 + (end_y - center_y) ** 2) ** 0.5)
                pygame.draw.circle(canvas, color, last_pos, radius_circle, radius)
            drawing=False

    pygame.display.update()

pygame.quit()