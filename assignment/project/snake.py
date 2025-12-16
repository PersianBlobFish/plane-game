import pygame
import sys
import random

# --- Settings ---
BLOCK_SIZE = 20          # Size of each grid square
GRID_WIDTH = 30          # Number of blocks horizontally
GRID_HEIGHT = 20         # Number of blocks vertically
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE

# Colors (R, G, B)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (40, 40, 40)



class Snake:
    def __init__(self):
        # Snake starts in the middle of the screen
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        # Moving right at the beginning
        self.direction = (1, 0)  # (dx, dy)

    def get_head(self):
        return self.body[0]

    def get_next_head(self):
        head_x, head_y = self.get_head()
        dx, dy = self.direction
        return head_x + dx, head_y + dy

    def change_direction(self, new_dir):
        """new_dir is (dx, dy); prevent 180° turn."""
        dx, dy = new_dir
        cur_dx, cur_dy = self.direction
        # Don't allow turning directly back into yourself
        if (dx, dy) == (-cur_dx, -cur_dy):
            return
        self.direction = (dx, dy)

    def move(self, grow=False):
        new_head = self.get_next_head()
        # Insert new head
        self.body.insert(0, new_head)
        # Remove tail if not growing
        if not grow:
            self.body.pop()

    def collides_with_walls(self):
        head_x, head_y = self.get_head()
        return (
            head_x < 0 or head_x >= GRID_WIDTH or
            head_y < 0 or head_y >= GRID_HEIGHT
        )

    def collides_with_self(self):
        head = self.get_head()
        return head in self.body[1:]

    def draw(self, surface):
        for (x, y) in self.body:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, color_select, rect)
            pygame.draw.rect(surface, DARK_GRAY, rect, 1)  # outline


class Food:
    def __init__(self, snake_body):
        self.position = (0, 0)
        self.randomize_position(snake_body)

    def randomize_position(self, snake_body):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(surface, color_select1, rect)


def draw_grid(surface):
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (0, y), (SCREEN_WIDTH, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    global color_select
    global color_select1
    color = [GREEN, RED, WHITE, BLUE, YELLOW]
    color_select = color[0]
    color_select1 = color[1]

    snake = Snake()
    food = Food(snake.body)
    score = 0
    game_over = False

    while True:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Movement keys
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

                # Restart on R when game over
                if game_over and event.key == pygame.K_r:
                    snake = Snake()
                    food = Food(snake.body)
                    score = 0
                    game_over = False

        if not game_over:
            # --- Game logic ---
            next_head = snake.get_next_head()

            # Check if snake will eat food
            will_eat = (next_head == food.position)

            # Move snake (grow if eats)
            snake.move(grow=will_eat)

            # If ate food, spawn new food and increase score
            if will_eat:
                if color_select == color[-1]:
                    color_select = color[0]
                color_select = color[color.index(color_select) + 1]
                if color_select1 == color[-1]:
                    color_select1 = color[0]
                color_select1 = color[color.index(color_select1) + 1]
                score += 1
                food.randomize_position(snake.body)

            # Collisions
            if snake.collides_with_walls() or snake.collides_with_self():
                game_over = True

        # --- Drawing ---
        screen.fill(BLACK)
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Game over text
        if game_over:
            over_text = font.render("Game Over! Press R to restart", True, WHITE)
            rect = over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(over_text, rect)

        pygame.display.flip()
        clock.tick(10)  # 10 frames per second (speed of the snake)


if __name__ == "__main__":
    main()
