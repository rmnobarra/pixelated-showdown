# Western Duel Game

This is a simple 2D Western duel game implemented in Python using Pygame. The game features an 8-bit style with pixel art graphics and sound effects for an immersive experience.

## Game Description

In this game, you play as a cowboy facing off against a computer-controlled opponent in a Western duel. The duel starts randomly, and you must quickly input a series of arrow key combinations to outshoot your opponent.

## Features

- 8-bit style pixel art graphics
- Background music and sound effects
- Random duel initiation
- Arrow key combination challenge
- Progress bar mechanic
- Player and computer character animations

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
