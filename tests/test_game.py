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
        game_instance = Game()
        return game_instance

def test_game_initialization(game, mock_sound_manager):
    assert game.WIDTH == 800
    assert game.HEIGHT == 600
    assert isinstance(game.player, Player)
    assert isinstance(game.computer, Computer)
    assert isinstance(game.graphics, Graphics)
    assert game.sound_manager == mock_sound_manager
    assert game.duel_started == False
    assert game.winner is None

def test_start_duel(game):
    game.start_duel()
    assert game.duel_started == True
    assert len(game.arrow_combination) == 4
    assert game.progress == 0
    assert game.player.state == "normal"
    assert game.computer.state == "normal"

def test_check_input_correct(game):
    game.start_duel()
    game.arrow_combination = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    
    for key in game.arrow_combination:
        game.check_input(key)
    
    assert game.winner == "Player"
    assert game.duel_started == False
    assert game.player.state == "shoot"
    assert game.computer.state == "hit"

def test_check_input_incorrect(game):
    game.start_duel()
    game.arrow_combination = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    
    wrong_keys = [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]
    for key in wrong_keys:
        game.check_input(key)
    
    assert game.winner == "Computer"
    assert game.duel_started == False
    assert game.player.state == "hit"
    assert game.computer.state == "shoot"

def test_end_duel(game):
    game.end_duel("Player")
    assert game.winner == "Player"
    assert game.duel_started == False
    assert game.player.state == "shoot"
    assert game.computer.state == "hit"
    assert game.animation_timer == game.ANIMATION_DURATION

def test_reset_game(game):
    game.winner = "Player"
    game.duel_started = True
    game.player_input = [pygame.K_UP, pygame.K_DOWN]
    game.progress = 50
    game.player.state = "shoot"
    game.computer.state = "hit"
    
    game.reset_game()
    
    assert game.duel_started == False
    assert game.winner is None
    assert game.player_input == []
    assert game.progress == 0
    assert game.player.state == "normal"
    assert game.computer.state == "normal"

@patch('random.random')
def test_update_start_duel(mock_random, game):
    mock_random.return_value = 0.005
    game.update()
    assert game.duel_started == True

@patch('random.random')
def test_update_no_start_duel(mock_random, game):
    mock_random.return_value = 0.02
    game.update()
    assert game.duel_started == False

def test_update_progress(game):
    game.duel_started = True
    initial_progress = game.progress
    game.update()
    assert game.progress > initial_progress

def test_update_end_duel_on_full_progress(game):
    game.duel_started = True
    game.progress = 99.9
    game.update()
    assert game.winner == "Computer"
    assert game.duel_started == False

# Update SoundManager tests
def test_sound_manager_initialization(mock_sound_manager):
    assert mock_sound_manager.background_music is not None
    assert mock_sound_manager.shoot_sound is not None

def test_sound_manager_play_background_music(mock_sound_manager):
    mock_sound_manager.play_background_music()
    mock_sound_manager.background_music.play.assert_called_once_with(-1)

def test_sound_manager_stop_background_music(mock_sound_manager):
    mock_sound_manager.stop_background_music()
    mock_sound_manager.background_music.stop.assert_called_once()

def test_sound_manager_play_shoot_sound(mock_sound_manager):
    mock_sound_manager.play_shoot_sound()
    mock_sound_manager.shoot_sound.play.assert_called_once()

# Add more tests as needed