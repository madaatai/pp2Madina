import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mouse Clock")


right_arm = pygame.image.load(r"C:\Users\Aldo\Desktop\github.python\python\lab7\clock_images\rightarm.png")
left_arm = pygame.image.load(r"C:\Users\Aldo\Desktop\github.python\python\lab7\clock_images\leftarm.png")
main_clock = pygame.image.load(r"C:\Users\Aldo\Desktop\github.python\python\lab7\clock_images\clock.png")
main_clock = pygame.transform.scale(main_clock, (800, 600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = minutes * 6 + (seconds / 60) * 6
    sec_angle = seconds * 6

    screen.fill((0, 0, 0))
    screen.blit(main_clock, (0, 0))

    rotated_rightarm = pygame.transform.rotate(right_arm, -min_angle)
    rightarm_rect = rotated_rightarm.get_rect(center=(800//2, 600//2))
    screen.blit(rotated_rightarm, rightarm_rect)

    rotated_leftarm = pygame.transform.rotate(left_arm, -sec_angle)
    leftarm_rect = rotated_leftarm.get_rect(center=(800//2, 600//2))
    screen.blit(rotated_leftarm, leftarm_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()