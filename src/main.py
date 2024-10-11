import sys
import os
import pygame
from pygame.locals import *

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.game import Game
from src.graphics import Graphics
from src.presentation import Presentation
from src.sound import SoundManager

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixelated Showdown")

# Colors
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title

# Create instances
graphics = Graphics(window, WINDOW_WIDTH, WINDOW_HEIGHT)
sound_manager = SoundManager()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def game_start_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                waiting = False
        
        graphics.draw_background()
        
        # Draw the game title
        draw_text("The Pixelated Showdown", title_font, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
        
        # Draw the "Press ENTER to start" message
        draw_text("Press ENTER to start", font, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
        
        pygame.display.flip()

def main():
    sound_manager.play_sound('background_music')
    game_start_screen()
    sound_manager.stop_music()
    
    presentation = Presentation(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    if presentation.run():
        sound_manager.play_sound('background_music')
        game = Game(window)
        game.run()
    else:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
