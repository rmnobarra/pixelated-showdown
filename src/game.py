import pygame
import random
import sys
import logging
from src.characters import Player, Computer
from src.graphics import Graphics
from src.sound import SoundManager
from src.utils import draw_message, draw_progress_bar

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Western Duel")
        self.clock = pygame.time.Clock()

        self.graphics = Graphics(self.screen, self.WIDTH, self.HEIGHT)
        try:
            self.sound_manager = SoundManager()
            self.sound_manager.play_background_music()
        except Exception as e:
            logging.error(f"Failed to initialize sound: {e}")
            self.sound_manager = None

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

    def run(self):
        if self.sound_manager:
            self.sound_manager.play_background_music()
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        if self.sound_manager:
            self.sound_manager.stop_background_music()
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if self.duel_started:
                    self.check_input(event.key)
                elif event.key == pygame.K_RETURN and self.winner:
                    self.reset_game()
                elif event.key == pygame.K_q:
                    return False
        return True

    def update(self):
        if not self.duel_started and not self.winner:
            if random.random() < 0.01:
                self.start_duel()

        if self.duel_started:
            self.progress += self.progress_speed
            if self.progress >= 100:
                self.end_duel("Computer")

        if self.animation_timer > 0:
            self.animation_timer -= 1
            if self.animation_timer == 0:
                if self.player.state == "shoot":
                    self.player.set_state("win")
                    self.computer.set_state("hit")
                    self.animation_timer = self.ANIMATION_DURATION * 2
                elif self.computer.state == "shoot":
                    self.computer.set_state("win")
                    self.player.set_state("hit")
                    self.animation_timer = self.ANIMATION_DURATION * 2
                elif self.player.state in ["hit", "win"] or self.computer.state in ["hit", "win"]:
                    self.player.set_state("normal")
                    self.computer.set_state("normal")

        self.player.update()
        self.computer.update()

    def draw(self):
        self.graphics.draw_background()
        self.player.draw(self.screen)
        self.computer.draw(self.screen)

        if self.winner:
            draw_message(self.screen, f"{self.winner} wins!", self.WIDTH, self.HEIGHT)
            draw_message(self.screen, "Press ENTER to retry or Q to quit", self.WIDTH, self.HEIGHT, y_offset=50)

        if self.duel_started:
            self.graphics.draw_arrow_combination(self.arrow_combination)
            draw_progress_bar(self.screen, self.progress_bar_x, self.progress_bar_y, 
                              self.progress_bar_width, self.progress_bar_height, self.progress)

        pygame.display.flip()

    def start_duel(self):
        self.duel_started = True
        self.arrow_combination = [random.choice(Graphics.ARROW_KEYS) for _ in range(4)]
        self.player_input = []
        self.progress = 0
        self.player.set_state("normal")
        self.computer.set_state("normal")

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
        if self.sound_manager:
            self.sound_manager.play_shoot_sound()
        self.duel_started = False
        if winner == "Player":
            self.player.set_state("shoot")
            self.computer.set_state("hit")
        else:
            self.player.set_state("hit")
            self.computer.set_state("shoot")
        self.animation_timer = self.ANIMATION_DURATION

    def reset_game(self):
        self.duel_started = False
        self.winner = None
        self.player_input = []
        self.progress = 0
        self.player.set_state("normal")
        self.computer.set_state("normal")