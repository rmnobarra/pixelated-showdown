import pygame
import random
import sys
import logging
import time
from src.characters import Player, Computer
from src.graphics import Graphics
from src.sound import SoundManager
from src.utils import draw_message, draw_progress_bar
from src.ending import EndingScene

logging.basicConfig(level=logging.INFO)

class Game:
    def __init__(self, window, debug_mode=False):
        pygame.init()
        pygame.mixer.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = window  # Use the window passed from main.py
        self.clock = pygame.time.Clock()

        self.graphics = Graphics(self.screen, self.WIDTH, self.HEIGHT)
        self.sound_manager = SoundManager()

        self.debug_mode = debug_mode
        self.ending_scene = EndingScene(self.screen, self.sound_manager)

        self.reset_game_state()

    def reset_game_state(self):
        self.player = Player(100, self.HEIGHT - 140, self.graphics)
        self.computer = Computer(self.WIDTH - 140, self.HEIGHT - 140, self.graphics)

        self.duel_started = False
        self.winner = None
        self.arrow_combination = []
        self.player_input = []
        self.progress = 0
        self.progress_speed = 0.5
        self.progress_bar_width = 200
        self.progress_bar_height = 20
        self.progress_bar_x = self.WIDTH - 250
        self.progress_bar_y = 50

        self.animation_timer = 0
        self.ANIMATION_DURATION = 30

        self.font = pygame.font.Font(None, 36)

        self.player_lives = 3  # Initialize player lives
        self.game_over_state = False  # New variable to track game over state
        
        self.current_chapter = 1
        self.enemy_lives = 2
        self.combination_length = 4

        self.enemies = [
            {"name": "Little Bit", "lives": 2, "combo": 4},
            {"name": "Brain Splitter", "lives": 2, "combo": 4},
            {"name": "Slaughterhouse", "lives": 4, "combo": 6},
            {"name": "Boot", "lives": 4, "combo": 8},
            {"name": "Few Locks", "lives": 4, "combo": 8},
            {"name": "Dry Lagoon", "lives": 6, "combo": 8},
            {"name": "Little Chinese", "lives": 6, "combo": 8},
            {"name": "Dried Gut", "lives": 8, "combo": 12}
        ]

        # Start playing background music
        self.sound_manager.stop_music()  # Stop any currently playing music
        self.sound_manager.stop_sound('the_final_sunset')  # Explicitly stop the ending song
        self.sound_manager.play_sound('background_music')

    def run(self):
        self.sound_manager.play_sound('background_music')
        running = True
        self.start_chapter()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        self.debug_mode = not self.debug_mode
                        print(f"Debug mode: {'ON' if self.debug_mode else 'OFF'}")
                    if self.debug_mode and event.key == pygame.K_F11:
                        self.debug_skip_to_end()
                    if self.game_over_state:
                        if event.key == pygame.K_RETURN:
                            self.reset_game_state()
                            self.start_chapter()
                        elif event.key == pygame.K_q:
                            running = False
                    elif self.duel_started:
                        self.check_input(event.key)
                    elif event.key == pygame.K_RETURN:
                        self.start_duel()
            self.update()
            self.draw()
            self.clock.tick(60)
        self.sound_manager.stop_music()
        pygame.quit()
        sys.exit()

    def update(self):
        if self.duel_started:
            self.progress += self.progress_speed
            if self.progress >= 100:
                self.end_duel("Computer")

        if self.animation_timer > 0:
            self.animation_timer -= 1
            if self.animation_timer == 0:
                if not self.game_over_state:
                    self.start_duel()  # Start a new duel if the game isn't over

        self.player.update()
        self.computer.update()

    def draw(self):
        self.graphics.draw_background()
        self.player.draw(self.screen)
        self.computer.draw(self.screen)

        # Draw chapter title at the top center
        draw_message(self.screen, f"Chapter {self.current_chapter}: {self.enemies[self.current_chapter-1]['name']}", self.WIDTH, self.HEIGHT, y_offset=-280)

        # Draw player lives on the left
        self.graphics.draw_player_lives(self.player_lives)

        # Draw enemy lives on the right
        self.graphics.draw_enemy_lives(self.enemy_lives)

        if self.game_over_state:
            draw_message(self.screen, "Game Over!", self.WIDTH, self.HEIGHT)
            draw_message(self.screen, "Press ENTER to retry or Q to quit", self.WIDTH, self.HEIGHT, y_offset=50)
        elif self.duel_started:
            # Draw arrow combination in the upper right
            self.graphics.draw_arrow_combination(self.arrow_combination)
            # Draw progress bar in the upper right, below the combination
            progress_bar_width = 200
            progress_bar_height = 15
            progress_bar_x = self.WIDTH - progress_bar_width - 10
            progress_bar_y = 70  # Just below the arrow combination
            draw_progress_bar(self.screen, progress_bar_x, progress_bar_y, 
                              progress_bar_width, progress_bar_height, self.progress)

        if self.debug_mode:
            debug_text = self.font.render("DEBUG MODE (F1): ON", True, (255, 0, 0))
            self.screen.blit(debug_text, (10, self.HEIGHT - 30))

        pygame.display.flip()

    def start_chapter(self):
        self.enemy_lives = self.enemies[self.current_chapter-1]['lives']
        self.combination_length = self.enemies[self.current_chapter-1]['combo']
        self.computer.set_enemy(self.enemies[self.current_chapter-1]['name'])
        
        # Display chapter information
        self.graphics.draw_background()
        draw_message(self.screen, f"Chapter {self.current_chapter}", self.WIDTH, self.HEIGHT, y_offset=-50)
        draw_message(self.screen, f"Enemy: {self.enemies[self.current_chapter-1]['name']}", self.WIDTH, self.HEIGHT, y_offset=0)
        draw_message(self.screen, f"Enemy Lives: {self.enemy_lives}", self.WIDTH, self.HEIGHT, y_offset=50)
        draw_message(self.screen, "Press ENTER to start the duel", self.WIDTH, self.HEIGHT, y_offset=100)
        pygame.display.flip()
        
        # Wait for player to press ENTER
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
        
        self.duel_started = False
        self.start_duel()

    def start_duel(self):
        self.sound_manager.play_sound('start')
        
        for i in range(3, 0, -1):
            self.graphics.draw_background()
            self.player.draw(self.screen)
            self.computer.draw(self.screen)
            self.draw_text(str(i), (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)
            pygame.display.flip()
            time.sleep(1)
        
        self.graphics.draw_background()
        self.player.draw(self.screen)
        self.computer.draw(self.screen)
        self.draw_text("DUEL!", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)
        pygame.display.flip()
        time.sleep(1)

        self.duel_started = True
        self.arrow_combination = [random.choice(Graphics.ARROW_KEYS) for _ in range(self.combination_length)]
        self.player_input = []
        self.progress = 0
        self.player.set_state("normal")
        self.computer.set_state("normal")

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def check_input(self, key):
        if key in Graphics.ARROW_KEYS:
            self.player_input.append(key)
            if self.player_input[-len(self.arrow_combination):] == self.arrow_combination:
                self.end_duel("Player")
            elif len(self.player_input) >= len(self.arrow_combination):
                if self.player_input[-len(self.arrow_combination):] != self.arrow_combination:
                    self.end_duel("Computer")

    def end_duel(self, winner):
        self.winner = winner
        self.sound_manager.play_sound('shoot')
        self.duel_started = False
        if winner == "Player":
            self.player.set_state("shoot")
            self.computer.set_state("hit")
            self.sound_manager.play_sound('win')
            self.enemy_lives -= 1
            if self.enemy_lives <= 0:
                self.next_chapter()
            else:
                self.animation_timer = self.ANIMATION_DURATION * 3
        else:
            self.player.set_state("hit")
            self.computer.set_state("shoot")
            self.sound_manager.play_sound('dead')
            self.player_lives -= 1
            if self.player_lives <= 0:
                self.game_over()
            else:
                self.animation_timer = self.ANIMATION_DURATION * 3

    def next_chapter(self):
        self.current_chapter += 1
        if self.current_chapter > 8:
            self.win_game()
        else:
            self.start_chapter()
        
        if self.debug_mode:
            print(f"Skipped to Chapter {self.current_chapter}")

    def win_game(self):
        self.game_over_state = True
        self.sound_manager.stop_music()  # Stop background music
        result = self.ending_scene.show_ending()
        if result == "new_game":
            self.sound_manager.stop_music()  # Stop ending music
            self.sound_manager.stop_sound('the_final_sunset')  # Explicitly stop the ending song
            self.reset_game_state()
            self.start_chapter()
        elif result == "quit":
            pygame.quit()
            sys.exit()

    def game_over(self):
        self.game_over_state = True
        self.duel_started = False

    def debug_skip_to_end(self):
        self.current_chapter = 8
        self.enemy_lives = 1
        self.combination_length = 12
        self.computer.set_enemy("Dried Gut")
        print(f"Debug: Skipped to final chapter")
        self.win_game()  # Call win_game() directly instead of start_chapter()
