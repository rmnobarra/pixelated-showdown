# Pixelated Showdown

Pixelated Showdown is a fast-paced, retro-style dueling game where players face off against computer opponents in a test of reflexes and timing.

## Game Overview

In Pixelated Showdown, players engage in pixel-art duels across multiple chapters. The game features:

- Quick-draw mechanics where timing is crucial
- Multiple computer opponents with increasing difficulty
- Retro-style pixel graphics
- Sound effects and background music
- A compelling storyline

## Project Structure

The project is organized as follows:

```
pixelated-showdown/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── game.py
│   ├── characters.py
│   ├── graphics.py
│   ├── sound.py
│   ├── presentation.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_game.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup

1. Ensure you have Python 3.x installed on your system.

2. Clone the repository:
   ```
   git clone https://github.com/rmnobarra/pixelated-showdown.git
   cd pixelated-showdown
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the game:
   ```
   python src/main.py
   ```

## How to Play

1. Start the game and progress through the chapters.
2. In each duel, you'll see a series of arrow icons representing the required combination.
3. Input the correct arrow key combination before the progress bar depletes.
4. Win the duel by entering the correct combination in time.
5. Lose if you input an incorrect combination or if the progress bar depletes.
6. Defeat all enemies across 8 chapters to win the game.

## Game Chapters

1. Chapter I - Little Bit 
2. Chapter II - Brain Splitter 
3. Chapter III - Slaughterhouse 
4. Chapter IV - Boot 
5. Chapter V - Few Locks
6. Chapter VI - Dry Lagoon 
7. Chapter VII - Little Chinese 
8. Chapter VIII - Dried Gut

## Controls

- Arrow keys (←↑→↓): Input the displayed combination during a duel
- ENTER: Start the game / Restart after a duel ends
- Q: Quit the game

## Dependencies

- Python 3.x
- Pygame 2.5.2

## Testing

To run the tests, use the following command:
```
pytest
```

## Debug Mode

The game includes a debug mode that can be enabled for testing and development purposes. When debug mode is active, the following options are available:

- N: Skip to the next chapter
- E: Skip to the end (final chapter)

Debug mode options are displayed on the screen during gameplay.

To enable or disable debug mode, modify the `self.debug_mode` variable in the `Game` class initialization (in `src/game.py`).

## Future Improvements

- Implement difficulty settings
- Create a high score system
- Add more varied animations and sound effects
- Expand the storyline and character backgrounds

Enjoy the showdown in Pixelated Showdown!

## Building Executables

To build executables for Windows or Linux, follow these steps:

1. Ensure you have PyInstaller installed:
   ```
   pip install pyinstaller
   ```

2. Run the build script:

   For Windows:
   ```
   python scripts/build.py
   ```

   For Linux:
   ```
   python3 scripts/build.py
   ```

3. The executable will be created in the `dist` folder.

## Installation

### Pre-built Executables

You can download pre-built executables for Windows and Linux from the latest GitHub Actions build:

1. Go to the [Actions tab](https://github.com/yourusername/pixelated-showdown/actions) in the GitHub repository.
2. Click on the latest successful workflow run.
3. Scroll down to the "Artifacts" section.
4. Download the appropriate artifact for your operating system:
   - `PixelatedShowdown-Windows.zip` for Windows
   - `PixelatedShowdown-Linux.zip` for Linux

After downloading, extract the zip file and run the executable:
- On Windows: Double-click `PixelatedShowdown.exe`
- On Linux: Open a terminal in the extracted directory and run `./PixelatedShowdown`

### Building from Source

If you prefer to build the game from source, follow these steps:

1. Ensure you have Python 3.x and pip installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/yourusername/pixelated-showdown.git
   cd pixelated-showdown
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the game:
   ```
   python src/main.py
   ```

## Building Executables Locally

To build executables on your local machine:

1. Ensure you have PyInstaller installed:
   ```
   pip install pyinstaller
   ```
2. Run the build script:
   - For Windows: `python scripts/build.py`
   - For Linux: `python3 scripts/build.py`
3. The executable will be created in the `dist` folder.
