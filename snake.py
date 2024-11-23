import pygame
import random
import sys

pygame.init()

# Initialize screen and game variables
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
snakeX = 800 / 2
snakeY = 600 / 2
flag = 1
foodX = (random.randrange(1, 799) // 10) * 10
foodY = (random.randrange(1, 599) // 10) * 10
clock = pygame.time.Clock()
changeX = 0
changeY = 0
sankelist = [(snakeX, snakeY)]
exit_font = pygame.font.Font(None, 100)
score_font = pygame.font.Font(None, 50)
score = 0


# Exit function to handle game over
def exit_game():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Render "GAME OVER" text
    game_exit_text = exit_font.render("GAME OVER", True, (255, 255, 255))
    game_exit_rect = game_exit_text.get_rect(center=(400, 200))  # Center the text
    screen.blit(game_exit_text, game_exit_rect)

    # Render the score text
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(400, 300))  # Center the text
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.update()

    # Pause for 3 seconds and quit
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


# Function to display and update the snake
def Display_snake():
    global snakeX, snakeY, foodX, foodY, sankelist, score

    # Update the snake's position
    snakeX = (snakeX + changeX) % 800
    snakeY = (snakeY + changeY) % 600

    # Check for collision with itself
    if (snakeX, snakeY) in sankelist[1:]:
        exit_game()

    # Update the snake's body
    sankelist.append((snakeX, snakeY))

    # Check if the snake eats food
    if foodX == snakeX and foodY == snakeY:
        foodX = (random.randrange(1, 799) // 10) * 10
        foodY = (random.randrange(1, 599) // 10) * 10
        score += 1
    else:
        del sankelist[0]  # Remove the tail if no food is eaten

    # Clear the screen and redraw the snake and food
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 100, 0), [foodX, foodY, 10, 10])
    for (x, y) in sankelist:
        pygame.draw.rect(screen, (255, 255, 255), [x, y, 10, 10])

    # Display score
    #

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and (flag == 1 or flag == 0):
                changeX = -10
                changeY = 0
                flag = 2
            if event.key == pygame.K_RIGHT and (flag == 1 or flag == 0):
                changeX = 10
                changeY = 0
                flag = 2
            if event.key == pygame.K_DOWN and (flag == 1 or flag == 2):
                changeX = 0
                changeY = 10
                flag = 0
            if event.key == pygame.K_UP and (flag == 1 or flag == 2):
                changeX = 0
                changeY = -10
                flag = 0

    Display_snake()
    clock.tick(10)
    pygame.display.update()

pygame.quit()
