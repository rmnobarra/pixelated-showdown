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
from src.ending import EndingScene

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
    sound_manager.play_sound('background_music')
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
    sound_manager.stop_music()

def debug_skip_to_end():
    global current_state
    print("Debug: Skipping to end")
    current_state = "ending"
    sound_manager.stop_music()
    sound_manager.play_sound('the_final_sunset')

def main():
    global current_state, player, enemy, chapter, game, debug_mode
    
    while True:
        game_start_screen()  # Show the start screen first
        
        current_state = "presentation"  # Initialize the current_state to "presentation"
        debug_mode = False  # Initialize debug_mode to False
        
        ending_scene = EndingScene(window, sound_manager)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        debug_mode = not debug_mode
                        print(f"Debug mode: {'ON' if debug_mode else 'OFF'}")
                    elif debug_mode and event.key == pygame.K_F11:
                        debug_skip_to_end()
                        if 'game' in locals():
                            game.win_game()  # Call win_game() if game object exists
            
            if current_state == "presentation":
                sound_manager.stop_music()  # Ensure all music is stopped
                sound_manager.play_sound('presentation_music')
                presentation = Presentation(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                if presentation.run():
                    sound_manager.fade_out(1000)  # Fade out the presentation music over 1 second
                    sound_manager.play_sound('background_music')
                    game = Game(window, debug_mode)  # Pass debug_mode to Game
                    current_state = "game"
                else:
                    pygame.quit()
                    sys.exit()
            elif current_state == "game":
                game.run()
                if game.debug_mode != debug_mode:  # Update debug_mode if changed in game
                    debug_mode = game.debug_mode
            elif current_state == "ending":
                result = ending_scene.show_ending()
                if result == "new_game":
                    sound_manager.stop_music()  # Stop all music before starting a new game
                    sound_manager.stop_sound('the_final_sunset')  # Explicitly stop the ending song
                    break  # Break the inner loop to restart the game
                elif result == "quit":
                    pygame.quit()
                    sys.exit()
            
            pygame.display.flip()

if __name__ == "__main__":
    main()
