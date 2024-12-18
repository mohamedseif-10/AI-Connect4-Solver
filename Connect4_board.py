import numpy as np


class ConnectFour:
    def __init__(self):
        self.board = self.Connect4Board()
        self.log_file_path = "connect_four_log.txt"

    def Connect4Board(self):
        return np.zeros((6, 7))

    def add_disc(self, col, player_id):
        """
        Add a disc to the board at the specified column for the given player.
        return false if the column is full
        return true if the disc is added successfully
        """
        if self.board[0][col] != 0:
            return False

        for row in range(5, -1, -1):  # rows are 5, 4, 3, 2, 1, 0
            if self.board[row][col] == 0:
                self.board[row][col] = player_id
                return True
        return False

    def check_winner(self, player_id):
        # Check horizontal
        for row in range(6):
            for col in range(4):  # 0, 1, 2, 3
                if np.all(self.board[row, col : col + 4] == player_id):
                    return True

        # Check vertical
        for row in range(3):
            for col in range(7):
                if np.all(self.board[row : row + 4, col] == player_id):
                    return True

        # Check diagonal (positive slope)
        for row in range(3, 6):
            for col in range(4):
                if np.all(
                    [self.board[row - i, col + i] == player_id for i in range(4)]
                ):  # check if all the elements in the list which is part of diagonal are equal to player_id
                    return True
        #     0 1 2 3 4 5 6
        #   -----------------
        # 0 - 1 0 0 0 0 0 0 -
        # 1 - 0 1 0 0 0 0 0 -
        # 2 - 0 0 1 0 0 0 0 -
        # 3 - 0 0 0 1 0 0 0 - -
        # 4 - 0 0 0 0 0 0 0 - -
        # 5 - 0 0 0 0 0 0 0 - -
        #     - - - -

        # Check diagonal (negative slope)
        for row in range(3):
            for col in range(4):
                if np.all(
                    [self.board[row + i, col + i] == player_id for i in range(4)]
                ):
                    return True

        return False

    def available_moves(self):  # return the available columns to play
        return [col for col in range(7) if self.board[0][col] == 0]

    def Save_game(self, winner=None):
        with open(self.log_file_path, "a") as file:
            if winner:
                file.write(f"Winner: Player {winner}\n")
            else:
                file.write("It's a draw!\n")
            file.write("Final Game State:\n")
            file.write(str(self.board))
            file.write("\n")
            file.write("-" * 30 + "\n")

    # Utility: Print the current game board
    def print_board(self):
        print(np.flip(self.board, axis=0))  # Flip to display in proper order


# Main game run

game = ConnectFour()
player_turn = np.random.choice([1, 2])
game_over = False

while not game_over:
    game.print_board()
    valid_moves = game.available_moves()

    print("Valid moves: ", end="")
    for i in range(7):
        if i in valid_moves:
            print(f"{i+1} ", end="")
    try:
        User_input_column = int(input(f"\nPlayer {player_turn}, choose a column: ")) - 1
    except ValueError:
        print("Please enter a valid column number.")
        continue

    if User_input_column not in valid_moves:
        print("Invalid move. Try again.")
        continue

    game.add_disc(User_input_column, player_turn)

    if game.check_winner(player_turn):
        game.print_board()
        game.Save_game(winner=player_turn)
        game_over = True
    elif not game.available_moves():
        game.print_board()
        print("It's a draw!")
        game.Save_game(winner=None)
        game_over = True
    else:
        player_turn = 3 - player_turn
        # Switch between player 1 and 2

print("Game over. Log file saved.")
