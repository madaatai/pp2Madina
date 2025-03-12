import pygame
import random

#Initialization pygame
pygame.init()

#Screen parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = 20  #Size of one cell
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Creating window for game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

#Installing font for game
font = pygame.font.SysFont("Verdana", 20)

#Direction of movements
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

#Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = RIGHT
        self.growing=False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        #Checking for crashing with wall
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            return False

        #Checking for crashing with itself
        if new_head in self.body:
            return False
        
        if not self.growing:
            self.body.pop()
        else:
            self.growing=False
            
        self.body.insert(0, new_head)  #Adding new head
        return True 

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        #Drawing snake
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def check_food_collision(self, food_pos):
        #Checking for food eating
        if self.body[0] == food_pos:
            return True
        return False
class Food:
    def __init__(self, snake_body):
        self.generate_food(snake_body)
        self.timer=300 #Lifetime of any food
    #Function for food generating
    def generate_food(self, snake_body):
        while True:
            self.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            self.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (self.x, self.y) not in snake_body:  #Generating food if it is not on snake body
                self.weight=random.randint(1, 3)
                self.timer=50
                break

#Main game cycle
def game_loop():
    snake = Snake()
    food = Food(snake.body)
    running = True
    clock = pygame.time.Clock()
    score = 0
    level = 1
    speed = 10

    while running:
        screen.fill(BLACK)

        #Showing scores and levels
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        #Snake movement
        if not snake.move():
            running = False  #Breaking game if snake does not move

        #Checking for eaten food
        if snake.check_food_collision((food.x, food.y)):
            score += food.weight
            snake.grow()
            food.generate_food(snake.body)

            #Switching levels
            if score % 4 == 0:
                level += 1
                speed += 2

        # Update food timer
        food.timer -= 1
        if food.timer <= 0:
            food.generate_food(snake.body)

        #Paintig food
        pygame.draw.rect(screen, RED if food.weight ==1 else BLUE, (food.x, food.y, CELL_SIZE, CELL_SIZE))

        #Drawing snake
        snake.draw()

        #Refreshing screen
        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

game_loop()