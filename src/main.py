import pygame
import sys, os
from pygame import mixer
import numpy as np
import random
# Initializing pygame and music
pygame.init()

def resource_path(relative_path):
    """Obtient le chemin absolu des ressources, fonctionne en dev et une fois packagé"""
    try:
        # PyInstaller crée un dossier temporaire défini comme _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # En développement, on utilise le dossier courant
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.mixer.init()
mixer.music.load(resource_path("assets/audio/Morning Stroll - Steven O'Brien (Must Credit, CC-BY, www.steven-obrien.net).mp3"))
mixer.music.set_volume(0.7)
mixer.music.play()


# font and score 
i=0
font = pygame.font.Font(resource_path('assets/fonts/Acme-Regular.ttf'), 40)
score_surface = font.render(str(i), False, (255, 255, 255))
#LIST FOR BEST SCORE
score_list=[]
score_list.append(0)



# Screen
screen = pygame.display.set_mode((800, 600))

# Controlling fps
clock = pygame.time.Clock()

# Caption
pygame.display.set_caption("Dodge it")

# Importing images
main_surface = pygame.image.load(resource_path('assets/images/bg.png'))
color = (255, 255, 255)
s = 3


def reset_game():
    global player_x, player_y, player_radius, fruit_x, fruit_y, fruit_alive, fruit_vel_x, fruit_vel_y, bullet_x, bullet_y
    player_x = 370
    player_y = 300
    player_radius = 30
    fruit_x = random.randrange(750)
    fruit_y = random.randrange(550)
    fruit_alive = True
    fruit_vel_x = random.uniform(-1, 1) * 5
    fruit_vel_y = random.uniform(-1, 1) * 5
    bullet_x = -20
    bullet_y = random.randrange(550)

run = True
pressed_keys = {}
player_x = 370
player_y = 300
player_radius = 30  # Initial radius of the player's circle

fruit_x = random.randrange(750)
fruit_y = random.randrange(550)
fruit_radius = 20
fruit_alive = True  # Flag to track fruit existence

# Velocity variables for the fruit
fruit_vel_x = random.uniform(-1, 1) * 5  # Random initial velocity in the x direction
fruit_vel_y = random.uniform(-1, 1) * 5  # Random initial velocity in the y direction
# Velocity variables for the bullet
bullet_vel = 10
# Bullet position
bullet_x = -20
bullet_y = random.randrange(550)

while run:
    
    score_surface = font.render(str(i), False,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for the QUIT event type
            run = False
        elif event.type == pygame.KEYDOWN:
            # Add the pressed key to the dictionary
            pressed_keys[event.key] = True
        elif event.type == pygame.KEYUP:
            # Remove the released key from the dictionary
            pressed_keys[event.key] = False

    # Clear the screen and draw the background
    screen.blit(main_surface, (0, 0))
    screen.blit(score_surface, (387,25))
    # Player movement
    if pressed_keys.get(pygame.K_RIGHT):
        player_radius += 0.1
        player_x += s
    if pressed_keys.get(pygame.K_UP):
        player_radius += 0.1
        player_y -= s
    if pressed_keys.get(pygame.K_DOWN):
        player_radius += 0.1
        player_y += s
    if pressed_keys.get(pygame.K_LEFT):
        player_radius += 0.1
        player_x -= s

    # Ensure the player stays within the screen boundaries
    player_x = max(player_x, 0)
    player_x = min(player_x, 800 - player_radius * 2)
    player_y = max(player_y, 0)
    player_y = min(player_y, 600 - player_radius * 2)

    # Calculate the distance between the fruit's center and the player's center
    dis_x = player_x + player_radius - fruit_x - fruit_radius
    dis_y = player_y + player_radius - fruit_y - fruit_radius
    dis = np.sqrt(dis_x ** 2 + dis_y ** 2)

    if dis < player_radius + fruit_radius:  # Check for collision
        i+=1
        if fruit_alive:
            player_radius = 30  # Reset the player radius
            fruit_alive = False  # Set the fruit to "dead"

    # Draw the fruit circle if alive
    if fruit_alive:
        pygame.draw.circle(screen, (0, 0, 0), (int(fruit_x), int(fruit_y)), fruit_radius)

        # Update fruit position using velocity for smooth movement
        fruit_x += fruit_vel_x
        fruit_y += fruit_vel_y

        # Bounce off the screen boundaries if the fruit goes outside
        if fruit_x < 20 or fruit_x > 800 - fruit_radius:
            fruit_vel_x *= -1
        if fruit_y < 20 or fruit_y > 600 - fruit_radius:
            fruit_vel_y *= -1

    else:  # If the fruit is dead, respawn it in a new random position with random velocity
        fruit_x = random.randrange(750)
        fruit_y = random.randrange(550)
        fruit_alive = True  # Set the fruit to "alive" again

        # Assign random velocities for smooth movement in a new direction
        fruit_vel_x = random.uniform(-1, 1) * 5
        fruit_vel_y = random.uniform(-1, 1) * 5

    # Draw the player circle with the updated position and size
    pygame.draw.circle(screen, color, (player_x + player_radius, player_y + player_radius), player_radius)

    # Let's make bullets, if the player touches a bullet, the game resets
    pygame.draw.circle(screen, (255,128,0), (bullet_x, bullet_y), 10)
    # Moving the bullet horizontally
    bullet_x += bullet_vel

    # Check if the bullet goes off the screen, then generate a new bullet
    if bullet_x > 800 + 10:
        bullet_x = -20
        bullet_y = random.randrange(550)

    # Check for collision between the bullet and the player
    dis_x_b = player_x + player_radius - bullet_x
    dis_y_b = player_y + player_radius - bullet_y
    dis_b = np.sqrt(dis_x_b ** 2 + dis_y_b ** 2)
    if dis_b < player_radius + 10:  # Bullet radius is 10
          # Player is shot, reset the game
        reset_game()
        score_list.append(i)
        i=0
    high_score = font.render(str(max(score_list)), False, color)
    screen.blit(font.render('High Score :', False, color),(10,10))
    screen.blit(high_score,(100,70))

    
    # Update the display
    pygame.display.update()
    clock.tick(90)
    
# Quit the game
pygame.quit()
