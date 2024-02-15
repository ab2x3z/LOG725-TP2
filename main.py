import pygame
import sys
import random
import os
from src.player import Player
from src.wall import Wall

pygame.init()

# Define colors
BG_COLOR = (153, 178, 178)

# Initialize Pygame
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create entities
player = Player()
walls = pygame.sprite.Group()
wall1 = Wall(350, 50, "regular")
wall2 = Wall(250, 50, "regular")
wall3 = Wall(150, 50, "regular")
wall4 = Wall(50, -50, "regular")
wall5 = Wall(-50, 50, "regular")
wall6 = Wall(-50, 150, "regular")
wall7 = Wall(-50, 250, "regular")
wall8 = Wall(450, 50, "blue")
wall9 = Wall(450, -50, "regular")
wall10 = Wall(550, 50, "regular")
wall11 = Wall(650, 50, "regular")
wall12 = Wall(750, 50, "regular")
wall13 = Wall(750, 150, "regular")
wall14 = Wall(750, 250, "regular")
wall15 = Wall(750, 350, "regular")
wall16 = Wall(650, 250, "red")
wall17 = Wall(650, 350, "blue")
wall18 = Wall(550, 250, "regular")
wall19 = Wall(550, 350, "regular")
wall20 = Wall(450, 350, "regular")
wall21 = Wall(350, 350, "regular")
wall22 = Wall(250, 350, "regular")
wall23 = Wall(250, 250, "regular")
wall24 = Wall(650, 450, "green")
wall25 = Wall(650, 550, "regular")
wall26 = Wall(550, 550, "regular")
wall27 = Wall(450, 550, "regular")
wall28 = Wall(350, 550, "regular")
wall29 = Wall(250, 550, "regular")
wall30 = Wall(150, 550, "regular")
wall31 = Wall(50, 550, "regular")
wall32 = Wall(-50, 550, "regular")
wall33 = Wall(-50, 450, "regular")
wall34 = Wall(-50, 350, "regular")
wall35 = Wall(550, 450, "blue")
wall36 = Wall(50, 250, "green")
wall37 = Wall(50, 450, "regular")
wall38 = Wall(150, 250, "regular")
wall39 = Wall(150, 450, "red")
wall40 = Wall(750, 550, "regular")

walls.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40)

# Menu section
########################################
# Function to display text
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Function to create buttons
def draw_button(text, font, color, hover_color, surface, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(surface, color, (x, y, width, height))

    draw_text(text, font, (0, 0, 0), surface, x + width // 2, y + height // 2)

# Function to start the game
def start_game():
    global playing
    playing = True

# Function to quit the game
def quit_game():
    global playing
    global menu
    playing = False
    menu = False

# Load background music
pygame.mixer.music.load('./assets/menuBackground.mp3')
# Set volume for the background music
pygame.mixer.music.set_volume(0.2)
# Start playing the background music in a loop
pygame.mixer.music.play(-1)

# Menu loop
menu = True
playing = False
while menu:
    if playing:
        menu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            playing = False

    screen.fill(BG_COLOR)

    font = pygame.font.Font(None, 69)
    # Draw buttons
    draw_button("Start", font, (240, 100, 100), (100, 100, 100), screen, 300, 200, 200, 100, start_game)
    draw_button("Quit", font, (240, 100, 100), (100, 100, 100), screen, 300, 350, 200, 100, quit_game)

    pygame.display.flip()
    clock.tick(30)
########################################

# Load background music
pygame.mixer.music.load('./assets/mainBackground.mp3')
# Set volume for the background music
pygame.mixer.music.set_volume(0.2)
# Start playing the background music in a loop
pygame.mixer.music.play(-1)

# Main game loop
# playing = True
win = False
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if not win:
        # before player update
        previous_x = player.rect.x
        previous_y = player.rect.y

        # player update 
        player.update()

        #check if player won
        if player.rect.x >= 750 and player.rect.y >= 450:
            win = True

        # check for collisions between player and walls
        wall_collisions = pygame.sprite.spritecollide(player, walls, False)
        for wall_collision in wall_collisions:
            print("Collided")

            # fall back to previous position
            player.rect.x = previous_x
            player.rect.y = previous_y
            break

        # check for collisions between walls and bullets
        for bullet in player.bullets:
            bullet_rect = pygame.Rect(bullet)
            for wall in walls:
                if bullet_rect.colliderect(wall):
                    if bullet.color == wall.color:
                        player.bullets.remove(bullet)
                        walls.remove(wall)
                        pygame.mixer.Sound('./assets/destroy.wav').play()
                    else:
                        player.bullets.remove(bullet)

        # draw
        screen.fill(BG_COLOR)

        # single sprites are drawn with screen.blit()
        screen.blit(player.image, (player.rect.x, player.rect.y))

        # groups of sprites can be drawn with group.draw()
        walls.draw(screen)
        player.bullets.draw(screen)

        # add color indicator
        indicator = pygame.Rect(0, 0, 60, 60)

        if player.color == (255, 0, 0):
            indicator = pygame.Rect(0, 0, 70, 70)

        elif player.color == (0, 255, 0):
            indicator = pygame.Rect(60, 0, 70, 70)

        elif player.color == (0, 0, 255):
            indicator = pygame.Rect(120, 0, 70, 70)

        pygame.draw.rect(screen, (0, 0, 0), indicator)

        # show remaining bullets
        if not player.redBulletUsed:
            square = pygame.Rect(10, 10, 50, 50)
            pygame.draw.rect(screen, (255, 0, 0), square)

        if not player.greenBulletUsed:
            square = pygame.Rect(70, 10, 50, 50)
            pygame.draw.rect(screen, (0, 255, 0), square)

        if not player.blueBulletUsed:
            square = pygame.Rect(130, 10, 50, 50)
            pygame.draw.rect(screen, (0, 0, 255), square)

    # Draw win screen if win condition is met
    else:
        win_screen = pygame.Rect(50, 50, 700, 500)
        pygame.draw.rect(screen, (255, 255, 255), win_screen)

        sound_files = [file for file in os.listdir('./assets/victory') if file.endswith('.wav')]
        randomVictorySound = random.choice(sound_files)
        pygame.mixer.Sound('./assets/victory/' + randomVictorySound).play()

        font = pygame.font.Font(None, 69)
        # Render text surface
        text_surface = font.render("You Win!", True, (0, 0, 0))

        # Get text rectangle and center it on the win screen
        text_rect = text_surface.get_rect(center=(800 // 2, 600 // 2))

        # Blit text onto win screen
        screen.blit(text_surface, text_rect)

        # Wait for user input to exit
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    waiting = False
                    playing = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()