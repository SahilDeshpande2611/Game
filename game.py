import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4
BOX_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find the Animal")

# Randomly place the animal
animal_position = random.randint(0, ROWS * COLS - 1)

# Game state
clicked_boxes = []

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            box_rect = pygame.Rect(col * BOX_SIZE, row * BOX_SIZE, BOX_SIZE, BOX_SIZE)
            pygame.draw.rect(win, WHITE, box_rect)
            pygame.draw.rect(win, BLACK, box_rect, 1)
            if row * COLS + col in clicked_boxes:
                if row * COLS + col == animal_position:
                    pygame.draw.rect(win, RED, box_rect)
                else:
                    pygame.draw.rect(win, BLACK, box_rect)

def check_win():
    if animal_position in clicked_boxes:
        return "lose"
    if len(clicked_boxes) == ROWS * COLS - 1:
        return "win"
    return "continue"

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // BOX_SIZE, y // BOX_SIZE
                box_index = row * COLS + col
                if box_index not in clicked_boxes:
                    clicked_boxes.append(box_index)
        
        win.fill(BLACK)
        draw_grid()
        game_state = check_win()
        if game_state == "lose":
            print("You Lose!")
            run = False
        elif game_state == "win":
            print("You Win!")
            run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
