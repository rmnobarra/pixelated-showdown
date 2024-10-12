import pygame
import os
import logging

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'background_music': pygame.mixer.Sound('assets/sounds/background_music.mp3'),
            'shoot': pygame.mixer.Sound('assets/sounds/shoot.wav'),
            'win': pygame.mixer.Sound('assets/sounds/win.wav'),
            'dead': pygame.mixer.Sound('assets/sounds/dead.wav'),
            'start': pygame.mixer.Sound('assets/sounds/start.wav'),
            'the_final_sunset': pygame.mixer.Sound('assets/sounds/the_final_sunset.mp3')
        }
        self.load_sounds()

    def load_sounds(self):
        sound_files = {
            'presentation_music': 'presentation_music.mp3',
            'game_over': 'game_over.wav',
            'final_sunset': 'the_final_sunset.mp3'
        }

        for sound_name, file_name in sound_files.items():
            file_path = os.path.join('assets', 'sounds', file_name)
            try:
                if sound_name in ['presentation_music', 'game_over']:
                    # We don't load these into self.sounds as they're handled differently
                    pygame.mixer.music.load(file_path)
                    logging.info(f"Loaded music: {sound_name}")
                else:
                    self.sounds[sound_name] = pygame.mixer.Sound(file_path)
                    logging.info(f"Loaded sound: {sound_name}")
            except pygame.error as e:
                logging.error(f"Couldn't load sound {sound_name}: {e}")

    def play_sound(self, sound_name):
        if sound_name in ['background_music', 'presentation_music']:
            try:
                pygame.mixer.music.load(os.path.join('assets', 'sounds', f'{sound_name}.mp3'))
                pygame.mixer.music.play(-1)
                logging.info(f"Playing music: {sound_name}")
            except pygame.error as e:
                logging.error(f"Couldn't play music {sound_name}: {e}")
        elif sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
                logging.info(f"Playing sound: {sound_name}")
            except pygame.error as e:
                logging.error(f"Couldn't play sound {sound_name}: {e}")
        else:
            logging.error(f"Sound not found: {sound_name}")

    def stop_music(self):
        pygame.mixer.music.stop()
        logging.info("Stopped music")

    def fade_out(self, time):
        pygame.mixer.music.fadeout(time)

    def stop_sound(self, sound_name):
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].stop()
                logging.info(f"Stopped sound: {sound_name}")
            except pygame.error as e:
                logging.error(f"Couldn't stop sound {sound_name}: {e}")
        else:
            logging.error(f"Sound not found: {sound_name}")
