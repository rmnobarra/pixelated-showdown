# Pixelated Showdown

Pixelated Showdown is a fast-paced, retro-style dueling game where players face off against a computer opponent in a test of reflexes and timing.

## Game Overview

In Pixelated Showdown, players engage in pixel-art duels. The game features:

- Quick-draw mechanics where timing is crucial
- A computer opponent with varying difficulty
- Retro-style pixel graphics
- Sound effects and background music

## Project Structure

```
western_duel/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── game.py
│   ├── characters.py
│   ├── graphics.py
│   ├── sound.py
│   └── utils.py
│
├── assets/
│   ├── images/
│   └── sounds/
│       ├── shoot.wav
│       └── background_music.mp3
│
├── README.md
└── requirements.txt
```

## Setup

1. Make sure you have Python installed on your system.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python src/main.py
   ```

## How to Play

1. Wait for the duel to start (it will begin randomly).
2. When the duel starts, you'll see a series of arrow icons at the top right of the screen.
3. Input the correct arrow key combination before the progress bar depletes.
4. If you input the correct combination in time, you win the duel!
5. If you input an incorrect combination or the progress bar depletes, you lose.
6. Press ENTER to play again or Q to quit after a duel ends.

## Controls

- Arrow keys (←↑→↓): Input the displayed combination during a duel
- ENTER: Restart the game after a duel ends
- Q: Quit the game

## Dependencies

- Python 3.x
- Pygame

## Future Improvements

- Add a scoring system
- Implement multiple rounds
- Create different difficulty levels
- Add more varied animations and sound effects

Enjoy the showdown in this Western Duel game!
