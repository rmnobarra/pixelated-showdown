# Western Duel Game

This is a simple text-based Western duel game implemented in Python. The game uses the Strategy design pattern and includes sound effects for an immersive experience.

## Project Structure

- `src/`: Contains the main game logic
- `tests/`: Contains unit tests
- `requirements/`: Contains project requirements and instructions
- `config/`: Contains game configuration files
- `assets/`: Contains audio files for sound effects

## Setup

1. Install the required dependencies:
   ```
   pip install pygame
   ```

2. Run the game:
   ```
   python src/western_duel.py
   ```

3. Run the tests:
   ```
   python -m unittest discover tests
   ```

## Game Rules

Two players take turns shooting at each other. The first player to hit their opponent wins the duel.

## Adding New Strategies

To add a new shooting strategy, create a new class that inherits from `ShootingStrategy` and implement the `shoot` method. Then, you can use this new strategy when creating `Player` objects.
