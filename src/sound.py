import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.load_sounds()

    def load_sounds(self):
        try:
            self.shoot_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "shoot.wav"))
            self.background_music = os.path.join("assets", "sounds", "background_music.mp3")
            print("Audio files loaded successfully")
        except pygame.error as e:
            print(f"Error loading audio files: {e}")
            print(f"Current working directory: {os.getcwd()}")
            print("Make sure 'shoot.wav' and 'background_music.mp3' are in the 'assets/sounds/' directory.")

    def play_shoot_sound(self):
        if hasattr(self, 'shoot_sound'):
            self.shoot_sound.play()

    def play_background_music(self):
        if hasattr(self, 'background_music'):
            pygame.mixer.music.load(self.background_music)
            pygame.mixer.music.play(-1)  # The -1 makes it loop indefinitely

    def stop_background_music(self):
        pygame.mixer.music.stop()