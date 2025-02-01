# TextBasedGame

A simple text-based adventure game.

## Story

The game starts with the player waking up in an unfamiliar place, surrounded by graves and a mysterious doll. The doll instructs the player to fight for their life. After choosing a class, the player battles their first opponent in an arena. The game progresses with battles and opportunities to upgrade items in a shop.

## Project Structure

- `assets/`: Contains game assets like text and icons.
    - `assets/text/`: Contains the game story in `story.txt`.
    - `assets/icons/`: Contains the game icon `game_icon.ico`.
- `build/`: Contains build artifacts.
- `game/`: Contains the game logic in Python.
    - `game/ability.py`: Defines player and enemy abilities.
    - `game/battle.py`: Handles battle logic.
    - `game/enemy.py`: Defines enemy characters.
    - `game/game_start.py`: Contains the game starting logic.
    - `game/inventory.py`: Manages player inventory.
    - `game/item.py`: Defines items in the game.
    - `game/player.py`: Defines the player character.
    - `game/shop.py`: Handles the game shop.
    - `game/story.py`: Manages the game story progression.
- `main.py`: The main entry point of the game.
- `main.spec`: PyInstaller spec file for building the game.

## How to Run

To run the game, execute `main.py`.