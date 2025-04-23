![Python 3.x Compatible](https://img.shields.io/badge/python-3.x-blue.svg)
[![License](https://img.shields.io/github/license/giansimone/tic-tac-toe-python)](https://github.com/giansimone/tic-tac-toe-python/blob/main/LICENSE)

# tic-tac-toe-python

A Python implementation of the Tic-Tac-Toe game.

## Overview

This is a simple text-based implementation of the Tic-Tac-Toe game in Python. The game allows two players to play against each other in a shell environment. The game board is represented as a 3x3 grid, and players take turns placing their marks (_X_ or _O_) on the grid. The game checks for a winner after each move and announces the result.

## How to Run

This project requires Python 3.x to run. You can run the game in your terminal or command prompt.

1. Clone the repository:
    ```bash
    git clone https://github.com/giansimone/tic-tac-toe-python.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tic-tac-toe-python
    ```
3. Run the game:
    ```bash
    python main.py
    ```
4. Follow the on-screen instructions to play the game.
5. Enter 'quit' or 'q' to exit the game at any time.

## Game Rules
- The game is played on a 3x3 grid.
- Players take turns placing their marks (_X_ or _O_) on the grid.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- If all nine squares are filled and no player has three in a row, the game is a draw.

## How to Play
1. The game starts with an empty grid.
2. The first player is randomly chosen.
3. Players take turns entering the row and column numbers where they want to place their mark.
  - The board positions are numbered as follows:
    ```
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ```
4. The game continues until there is a winner or the game ends in a draw.
5. The game announces the result and asks if you want to play again.
6. Enter 'y' or 'n' to continue or exit the game.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
