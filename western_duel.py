import pygame
import random
import sys
import os  # Add this import at the top of your file

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Add this line to create the clock object
clock = pygame.time.Clock()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Western Duel")

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Pixel art generation function
def create_pixel_art(width, height, color, pixels):
    surface = pygame.Surface((width, height))
    surface.fill(WHITE)
    pixel_size = min(width // len(pixels[0]), height // len(pixels))
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            if pixel:
                pygame.draw.rect(surface, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))
    return surface

# Generate pixel art for characters and events

player_pixels = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Update the computer_pixels to make it look more villainous
computer_pixels = [
    [0,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,0,0],
    [1,0,1,1,1,0,0,0],
    [1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,0,0,1],
    [0,0,1,1,1,0,0,0],
    [0,0,1,0,1,0,0,0],
]

# Add new pixel art for player animations
player_shoot_pixels = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

player_win_pixels = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

player_hit_pixels = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0]
]

# Add new pixel art for computer animations
computer_shoot_pixels = [
    [0,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,0,0],
    [1,0,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,1,1,1,0,0,1],
    [0,0,1,1,1,0,0,0],
    [0,0,1,0,1,0,0,0],
]

computer_win_pixels = [
    [0,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,0,0],
    [1,0,1,1,1,0,1,0],
    [1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,0,0,1],
    [0,1,1,0,1,1,0,0],
    [1,0,1,0,1,0,1,0],
]

computer_hit_pixels = [
    [0,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,0,0],
    [1,0,1,1,1,0,0,0],
    [1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,0,0,1],
    [0,1,0,1,0,1,0,0],
    [1,0,0,1,0,0,1,0],
]

# Create pixel art images for characters
player = create_pixel_art(50, 50, BLACK, player_pixels)
computer = create_pixel_art(50, 50, BLACK, computer_pixels)

# Create pixel art images for player animations
player_shoot = create_pixel_art(50, 50, BLACK, player_shoot_pixels)
player_win = create_pixel_art(50, 50, BLACK, player_win_pixels)
player_hit = create_pixel_art(50, 50, BLACK, player_hit_pixels)

# Create pixel art images for computer animations
computer_shoot = create_pixel_art(50, 50, BLACK, computer_shoot_pixels)
computer_win = create_pixel_art(50, 50, BLACK, computer_win_pixels)
computer_hit = create_pixel_art(50, 50, BLACK, computer_hit_pixels)

# Create a simple background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(SKY_BLUE)
pygame.draw.rect(background, GROUND_BROWN, (0, HEIGHT - 100, WIDTH, 100))

# Load sound effects and music
try:
    shoot_sound = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("background_music.mp3")
    print("Audio files loaded successfully")
except pygame.error as e:
    print(f"Error loading audio files: {e}")
    print(f"Current working directory: {os.getcwd()}")
    print("Make sure 'shoot.wav' and 'background_music.mp3' are in the same directory as the script.")
    sys.exit()

# Start playing the background music
pygame.mixer.music.play(-1)  # The -1 makes it loop indefinitely

# Game variables
player_x = 100
computer_x = WIDTH - 140
character_y = HEIGHT - 140
duel_started = False
winner = None

# New variables for arrow key challenge
arrow_keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]
arrow_key_names = {pygame.K_LEFT: "LEFT", pygame.K_UP: "UP", pygame.K_RIGHT: "RIGHT", pygame.K_DOWN: "DOWN"}
arrow_combination = []
player_input = []
progress_bar_width = 200
progress_bar_height = 20
progress_bar_x = WIDTH - 250
progress_bar_y = 50
progress = 0
progress_speed = 0.5

# Add new variables for player animation
player_state = "normal"
animation_timer = 0
ANIMATION_DURATION = 30  # frames

# Add a new variable for computer animation
computer_state = "normal"

def draw_scene():
    screen.blit(background, (0, 0))
    
    # Draw player based on current state
    if player_state == "normal":
        screen.blit(player, (player_x, character_y))
    elif player_state == "shoot":
        screen.blit(player_shoot, (player_x, character_y))
    elif player_state == "win":
        screen.blit(player_win, (player_x, character_y))
    elif player_state == "hit":
        screen.blit(player_hit, (player_x, character_y))
    
    # Draw computer based on current state
    if computer_state == "normal":
        screen.blit(computer, (computer_x, character_y))
    elif computer_state == "shoot":
        screen.blit(computer_shoot, (computer_x, character_y))
    elif computer_state == "win":
        screen.blit(computer_win, (computer_x, character_y))
    elif computer_state == "hit":
        screen.blit(computer_hit, (computer_x, character_y))
    
    if winner:
        font = pygame.font.Font(None, 74)
        text = font.render(f"{winner} wins!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        draw_message("Press ENTER to retry or Q to quit")

    if duel_started:
        draw_arrow_combination()
        draw_progress_bar()

def start_duel():
    global duel_started, arrow_combination, progress, player_input
    duel_started = True
    arrow_combination = [random.choice(arrow_keys) for _ in range(4)]
    player_input = []
    progress = 0
    print(f"Duel started, arrow combination: {[arrow_key_names[k] for k in arrow_combination]}")

def draw_arrow_combination():
    left_arrow = [
        [0,0,1,0,0],
        [0,1,1,0,0],
        [1,1,1,1,1],
        [0,1,1,0,0],
        [0,0,1,0,0],
    ]
    
    right_arrow = [
        [0,0,1,0,0],
        [0,0,1,1,0],
        [1,1,1,1,1],
        [0,0,1,1,0],
        [0,0,1,0,0],
    ]
    
    up_arrow = [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [1,0,1,0,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ]
    
    down_arrow = [
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,0,1,0,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
    ]

    arrow_images = {
        pygame.K_LEFT: create_pixel_art(25, 25, BLACK, left_arrow),
        pygame.K_UP: create_pixel_art(25, 25, BLACK, up_arrow),
        pygame.K_RIGHT: create_pixel_art(25, 25, BLACK, right_arrow),
        pygame.K_DOWN: create_pixel_art(25, 25, BLACK, down_arrow)
    }
    
    for i, key in enumerate(arrow_combination):
        screen.blit(arrow_images[key], (WIDTH - 250 + i * 35, 20))

def draw_progress_bar():
    pygame.draw.rect(screen, WHITE, (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height))
    pygame.draw.rect(screen, RED, (progress_bar_x, progress_bar_y, progress_bar_width * (progress / 100), progress_bar_height))

def check_input(key):
    global player_input, winner, duel_started, player_state, computer_state, animation_timer
    if key in arrow_keys:
        player_input.append(key)
        if player_input[-len(arrow_combination):] == arrow_combination:
            winner = "Player"
            shoot_sound.play()
            duel_started = False
            player_state = "shoot"
            computer_state = "hit"
            animation_timer = ANIMATION_DURATION
        elif len(player_input) >= len(arrow_combination):
            if player_input[-len(arrow_combination):] != arrow_combination:
                winner = "Computer"
                shoot_sound.play()
                duel_started = False
                player_state = "hit"
                computer_state = "shoot"
                animation_timer = ANIMATION_DURATION

# Add a new function to display game messages
def draw_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text, text_rect)

# Modify the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key} ({pygame.key.name(event.key)})")  # Debug print
            if duel_started:
                check_input(event.key)
            elif event.key == pygame.K_RETURN and winner:
                # Reset the game
                duel_started = False
                winner = None
                player_input = []
                progress = 0
            elif event.key == pygame.K_q:
                running = False

    if not duel_started and not winner:
        if random.random() < 0.01:  # 1% chance per frame to start the duel
            start_duel()
            player_state = "normal"
            print("Duel started randomly")  # Debug print

    if duel_started:
        progress += progress_speed
        if progress >= 100:
            winner = "Computer"
            shoot_sound.play()
            duel_started = False
            player_state = "hit"
            computer_state = "shoot"
            animation_timer = ANIMATION_DURATION

    # Handle player and computer animation
    if animation_timer > 0:
        animation_timer -= 1
        if animation_timer == 0:
            if player_state == "shoot":
                player_state = "win"
                computer_state = "hit"
                animation_timer = ANIMATION_DURATION * 2  # Longer duration for win animation
            elif computer_state == "shoot":
                computer_state = "win"
                player_state = "hit"
                animation_timer = ANIMATION_DURATION * 2  # Longer duration for win animation
            elif player_state in ["hit", "win"] or computer_state in ["hit", "win"]:
                player_state = "normal"
                computer_state = "normal"

    draw_scene()
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()  # Stop the music when the game ends
pygame.quit()
sys.exit()