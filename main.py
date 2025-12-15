import pygame
from sys import exit
import random
import math

pygame.init()
clock = pygame.time.Clock()

# Window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

# Audio
pygame.mixer.music.load("assets/Vine Boom.mp3")
pygame.mixer.music.set_volume(0.2)

# Images
plane_images = [pygame.image.load("assets/plane_down.png"),
               pygame.image.load("assets/plane_mid.png"),
               pygame.image.load("assets/plane_up.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_tower_images = pygame.image.load("assets/tower_top.png")
bottom_tower_images = pygame.image.load("assets/tower_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game
scroll_speed = 2
plane_start_position = (100, 250)
score = 0
font = pygame.font.SysFont('Segoe', 26)
game_stopped = True

bg = skyline_image.convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(win_width / bg_width) + 1

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = plane_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.is_alive = True

    def update(self, user_input):
        # Animate Plane
        if self.is_alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = plane_images[self.image_index // 10]

        # Gravity
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # Rotate Plane
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        # User Input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.is_alive:
            self.flap = True
            self.vel = -7


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image, tower_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.tower_type = tower_type

    def update(self):
        # Move tower
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

        # Score
        global score
        if self.tower_type == 'bottom':
            if plane_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if plane_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Main Game Loop
def main():
    global score, scroll

    # Initiate plane
    plane = pygame.sprite.GroupSingle()
    plane.add(Plane())

    # Setup towers
    tower_timer = 0
    towers = pygame.sprite.Group()

    # Instantiate initial ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    run = True
    while run:
        # Quit
        quit_game()

        # Reset frame
        window.fill((0, 0, 0))

        # User input
        user_input = pygame.key.get_pressed()

        # Draw background
        for i in range(0, tiles):
            window.blit(skyline_image, (i * bg_width + scroll, 0))

        scroll -= 0.7

        # Reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        # Spawn ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground))

        # Draw - plane, tower and ground
        towers.draw(window)
        ground.draw(window)
        plane.draw(window)

        # Show score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))

        # Update
        if plane.sprite.is_alive:
            towers.update()
            ground.update()
        plane.update(user_input)

        # Collision detection
        collision_towers = pygame.sprite.spritecollide(plane.sprites()[0], towers, False)
        collision_ground = pygame.sprite.spritecollide(plane.sprites()[0], ground, False)
        if collision_towers or collision_ground:
            pygame.mixer.music.play()
            plane.sprite.is_alive = False
            if collision_ground:
                window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2,
                                              win_height // 2 - game_over_image.get_height() // 2))
                if user_input[pygame.K_r]:
                    score = 0
                    break

        # Spawn towers
        if tower_timer <= 0 and plane.sprite.is_alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_tower_images.get_height()
            towers.add(Tower(x_top, y_top, top_tower_images, 'top'))
            towers.add(Tower(x_bottom, y_bottom, bottom_tower_images, 'bottom'))
            tower_timer = random.randint(180, 250)
        tower_timer -= 1

        clock.tick(60)
        pygame.display.update()


# Menu
def menu():
    global game_stopped

    while game_stopped:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))
        window.blit(ground_image, (0, 520))
        window.blit(plane_images[0], (100, 250))
        window.blit(start_image, (win_width // 2 - start_image.get_width() // 2,
                                  win_height // 2 - start_image.get_height() // 2))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()


menu()