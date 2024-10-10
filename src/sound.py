import pygame
import os
import logging

class SoundManager:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        sound_dir = os.path.join(project_root, 'assets', 'sounds')

        self.background_music = self._load_sound(os.path.join(sound_dir, 'background_music.mp3'))
        self.shoot_sound = self._load_sound(os.path.join(sound_dir, 'shoot.wav'))

    def _load_sound(self, path):
        try:
            return pygame.mixer.Sound(path)
        except FileNotFoundError:
            logging.warning(f"Sound file not found: {path}")
            return self._create_dummy_sound()

    def _create_dummy_sound(self):
        buffer = bytearray(22050)  # 1 second of silence (22050 is the sample rate)
        return pygame.mixer.Sound(buffer=buffer)

    def play_background_music(self):
        if self.background_music:
            self.background_music.play(-1)  # -1 means loop indefinitely

    def stop_background_music(self):
        if self.background_music:
            self.background_music.stop()

    def play_shoot_sound(self):
        if self.shoot_sound:
            self.shoot_sound.play()