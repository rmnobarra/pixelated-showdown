import pytest
import pygame
from unittest.mock import Mock, patch
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.game import Game
from src.characters import Player, Computer
from src.graphics import Graphics
from src.sound import SoundManager

@pytest.fixture
def mock_sound_manager():
    with patch('src.sound.pygame.mixer.Sound', return_value=Mock()) as mock_sound:
        sound_manager = SoundManager()
        yield sound_manager

@pytest.fixture
def game(mock_sound_manager):
    with patch('pygame.display.set_mode'), \
         patch('pygame.mixer.init'), \
         patch('src.game.SoundManager', return_value=mock_sound_manager):
        game_instance = Game(Mock(), debug_mode=True)
        return game_instance

class TestGameInitialization:
    def test_game_attributes(self, game, mock_sound_manager):
        assert game.WIDTH == 800
        assert game.HEIGHT == 600
        assert isinstance(game.player, Player)
        assert isinstance(game.computer, Computer)
        assert isinstance(game.graphics, Graphics)
        assert game.sound_manager == mock_sound_manager
        assert game.duel_started == False
        assert game.winner is None

    def test_initial_game_state(self, game):
        assert game.player_lives == 3
        assert game.game_over_state == False
        assert game.current_chapter == 1
        assert game.enemy_lives == 2
        assert game.combination_length == 4

class TestGameMechanics:
    def test_start_duel(self, game):
        game.start_duel()
        assert game.duel_started == True
        assert len(game.arrow_combination) == 4
        assert game.progress == 0
        assert game.computer.state == "normal"

    def test_check_input_correct(self, game):
        game.start_duel()
        game.arrow_combination = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        
        for key in game.arrow_combination:
            game.check_input(key)
        
        assert game.winner == "Player"
        assert game.duel_started == False
        assert game.player.state == "shoot"
        assert game.computer.state == "hit"

    def test_check_input_incorrect(self, game):
        game.start_duel()
        game.arrow_combination = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        
        wrong_keys = [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]
        for key in wrong_keys:
            game.check_input(key)
        
        assert game.winner == "Computer"
        assert game.duel_started == False
        assert game.player.state == "hit"
        assert game.computer.state == "shoot"

    def test_end_duel(self, game):
        game.end_duel("Player")
        assert game.winner == "Player"
        assert game.duel_started == False
        assert game.player.state == "shoot"
        assert game.computer.state == "hit"
        assert game.animation_timer == game.ANIMATION_DURATION * 3

    def test_reset_game(self, game):
        game.winner = "Player"
        game.duel_started = True
        game.player_input = [pygame.K_UP, pygame.K_DOWN]
        game.progress = 50
        game.player.state = "shoot"
        game.computer.state = "hit"
        
        game.reset_game_state()
        
        assert game.duel_started == False
        assert game.winner is None
        assert game.player_input == []
        assert game.progress == 0
        assert game.computer.state == "normal"

class TestGameUpdate:
    @patch('random.random')
    def test_update_start_duel(self, mock_random, game):
        mock_random.return_value = 0.005
        game.update()
        assert game.duel_started == True

    @patch('random.random')
    def test_update_no_start_duel(self, mock_random, game):
        mock_random.return_value = 0.02
        game.update()
        assert game.duel_started == False

    def test_update_progress(self, game):
        game.duel_started = True
        initial_progress = game.progress
        game.update()
        assert game.progress > initial_progress

    def test_update_end_duel_on_full_progress(self, game):
        game.duel_started = True
        game.progress = 99.9
        game.update()
        assert game.winner == "Computer"
        assert game.duel_started == False

class TestSoundManager:
    def test_sound_manager_initialization(self, mock_sound_manager):
        assert 'background_music' in mock_sound_manager.sounds
        assert 'shoot' in mock_sound_manager.sounds

    def test_sound_manager_play_sound(self, mock_sound_manager):
        mock_sound_manager.play_sound('shoot')
        mock_sound_manager.sounds['shoot'].play.assert_called_once()

    @patch('pygame.mixer.music')
    def test_sound_manager_play_music(self, mock_mixer_music, mock_sound_manager):
        mock_sound_manager.play_sound('background_music')
        mock_mixer_music.load.assert_called_once()
        mock_mixer_music.play.assert_called_once_with(-1)

    @patch('pygame.mixer.music')
    def test_sound_manager_stop_music(self, mock_mixer_music, mock_sound_manager):
        mock_sound_manager.stop_music()
        mock_mixer_music.stop.assert_called_once()

class TestGameProgression:
    def test_next_chapter(self, game):
        initial_chapter = game.current_chapter
        game.next_chapter()
        assert game.current_chapter == initial_chapter + 1
        assert game.enemy_lives == game.enemies[game.current_chapter-1]['lives']
        assert game.combination_length == game.enemies[game.current_chapter-1]['combo']

    def test_game_over(self, game):
        game.game_over()
        assert game.game_over_state == True
        assert game.duel_started == False

    @patch('src.game.EndingScene')
    def test_win_game(self, mock_ending_scene, game):
        mock_ending_scene.return_value.show_ending.return_value = "new_game"
        game.win_game()
        assert game.game_over_state == True
        mock_ending_scene.return_value.show_ending.assert_called_once()

class TestDebugMode:
    def test_debug_skip_to_end(self, game):
        game.debug_skip_to_end()
        assert game.current_chapter == 8
        assert game.enemy_lives == 1
        assert game.combination_length == 12
        assert game.computer.current_enemy == "Dried Gut"
