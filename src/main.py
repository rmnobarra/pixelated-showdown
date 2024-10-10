import sys
import os
import pygame  # Add this import

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.game import Game  # Change this line

def main():
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()