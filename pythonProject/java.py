
import pygame
import random
import pygame
# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Race Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the car and obstacles
car_image = pygame.image.load("car.png")
car_width = car_image.get_width()
car_height = car_image.get_height()
car_x = (WIDTH - car_width) // 2
car_y = HEIGHT - car_height - 10
obstacle_width = 80
obstacle_height = 60
obstacle_speed = 5
obstacle_gap = 200
obstacle_y = -obstacle_height
obstacle_x = random.randint(0, WIDTH - obstacle_width)
score = 0

# Load the font
font = pygame.font.Font(None, 36)

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= 20
            elif event.key == pygame.K_RIGHT:
                car_x += 20

    # Update the game state
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1

    # Check for collision with the car
    if obstacle_y + obstacle_height > car_y and obstacle_y < car_y + car_height and obstacle_x + obstacle_width > car_x and obstacle_x < car_x + car_width:
        game_over = True

    # Draw the game world
    window.fill(WHITE)
    window.blit(car_image, (car_x, car_y))
    pygame.draw.rect(window, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()