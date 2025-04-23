"""
A simple Tic-Tac-Toe game implementation in Python.
"""
import os
import time
import random


class Board:
    """A class to represent the Tic-Tac-Toe board."""

    def __init__(self):
        """Initialise the board with empty spaces."""
        self.reset()

    def __str__(self):
        """Return a string representation of the board."""
        return '\n'.join([
            f' {self.board[0]} | {self.board[1]} | {self.board[2]} ',
            '-----------',
            f' {self.board[3]} | {self.board[4]} | {self.board[5]} ',
            '-----------',
            f' {self.board[6]} | {self.board[7]} | {self.board[8]} '
        ])

    def __getitem__(self, position: int) -> str:
        """Get the value at a specific position on the board."""
        return self.board[position]

    def reset(self):
        """Reset the board to empty spaces."""
        self.round = 1
        self.board = [' ' for _ in range(9)]

    def update(self, position: int, player: str) -> bool:
        """Update the board with the player's move.
        
        Args:
            position (int): The position on the board (1-9).
            player (str): The player's symbol ('X' or 'O').
        
        Returns:
            bool: True if the move was successful, False if the position is already occupied.
        """
        if self.board[position - 1] == ' ':
            self.board[position - 1] = player
            self.round += 1
            return True
        return False


class TicTacToe:
    """ A class to represent a Tic-Tac-Toe game. """

    def __init__(self):
        """ Initialise the game board and the current player. """
        self.running = True
        self.current_player = None
        self.winner = None
        self.board = Board()
        self._select_first_player()

    def _clear_screen(self):
        """ Clear the console screen. """
        os.system('cls' if os.name == 'nt' else 'clear')

    def _print_instructions(self):
        """ Print the game instructions. """
        print('Welcome to Tic-Tac-Toe!')
        print('\n-------------------------------------\n')
        print('Instructions:')
        print('  1. The game is played on a 3x3 grid.')
        print('  2. Players take turns placing their mark (X or O) in an empty cell.')
        print('  3. The first player to get 3 marks in a row wins.')
        print('  4. If all cells are filled, the game is a draw.')
        print("  5. Enter 'quit' or 'q' at any time to quit the game.")
        print('\n-------------------------------------\n')
        print('The board positions are numbered as follows:\n')
        print(' 1 | 2 | 3 ')
        print('-----------')
        print(' 4 | 5 | 6 ')
        print('-----------')
        print(' 7 | 8 | 9 ')
        input('\nPress Enter to start the game...')

    def _draw_board(self):
        """ Draw the current state of the game board. """
        self._clear_screen()
        print('Tic-Tac-Toe\n')
        print(self.board)
        print('\n')

    def _select_first_player(self):
        """ Randomly select the first player. """
        if random.randint(0, 1) == 0:
            self.current_player = 'X'
        else:
            self.current_player = 'O'

    def _reset_game(self):
        """ Reset the game board and select the first player. """
        self.board.reset()
        self.winner = None
        self._select_first_player()

    def _get_current_player_move(self):
        """ Get the current player's move. """
        while True:
            move = input(f'Player {self.current_player}, enter your move (1-9): ')
            if move.isdigit():
                move = int(move)
                if 1 <= move <= 9 and self.board[move - 1] == ' ':
                    self.board.update(move, self.current_player)
                    return
            elif move.lower() == 'q' or move.lower() == 'quit':
                print('Exiting the game.')
                for i in range(3):
                    self._draw_board()
                    print('Thanks for playing!')
                    print('Exiting the game.' + '.' * i)
                    time.sleep(0.5)
                self.running = False
                return
            print('Invalid input.')

    def _check_winner(self):
        """ Check if there is a winner. """
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def _update_game_state(self):
        """ Update the game state after each move. """
        if self._check_winner():
            self.winner = self.current_player
            self.running = False
        elif ' ' not in self.board:
            self.winner = 'Draw'
            self.running = False
        else:
            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def _play_again(self):
        """ Ask the player if they want to play again. """
        while True:
            play_again = input('Do you want to play again? [Y/n] ').lower()
            if play_again in ('y', ''):
                self._reset_game()
                self._draw_board()
                self.running = True
                return
            if play_again == 'n':
                return
            print('Invalid input. Please enter [Y/n].')

    def main(self):
        """ Main method to run the game loop. """
        self._clear_screen()
        self._print_instructions()

        self._draw_board()

        while self.running:
            self._get_current_player_move()

            self._update_game_state()

            self._draw_board()

            if not self.running and self.winner:
                if self.winner == 'Draw':
                    print('The game is a draw!')
                elif self.winner:
                    print(f'Player {self.winner} wins!')
                self._play_again()

        self._clear_screen()


if __name__ == '__main__':
    game = TicTacToe()
    game.main()
