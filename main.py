import re
from Board import Board


def play(board_size=10, bombs=10):
    #  create the board and plant the bombs
    board = Board(board_size, bombs)
    #  show the user the board and ask for where they want to dig
    safe_dig = True  # set the initial dig to be true

    while len(board.dug_cells) < board.board_size ** 2 - board.bombs:
        print(board)
        row_input = -1
        column_input = -1
        valid_row_input = False
        valid_column_input = False

        while not valid_row_input:
            try:
                row_input = int(input('Where would you like to dig? input a row [0-9]: ').split()[0])
                if 0 < row_input <= 9:
                    valid_row_input = True
            except:
                pass

            # if the user enters an invalid character

        while not valid_column_input:
            try:
                column_input = int(input('Where would you like to dig? input a column [0-9]: ').split()[0])
                if column_input < 0 and column_input <= 9:
                    valid_column_input = True
            except:
                pass

        row, col = row_input, column_input
        if row < 0 or row >= board.board_size or col < 0 or col >= board.board_size:
            print("Location  is out of bounds")
            continue

        #  if the location is valid
        safe_dig = board.dig(row, col)
        #  if the location is a bomb, game over!
        if not safe_dig:
            break
    if safe_dig:
        print('***YOUR AN EXPERT EXCAVATOR!!!***')
    # board.dug_cells = [(r, c) for r in range(board.board_size) for c in range(board.board_size)]
    # print(board)
    else:
        print('---BOOM!!! THAT\'S ALL YOU HEAR---')
        print('have a look where the bombs where =)')
        # take every row and col value and
        board.dug_cells = [(r, c) for r in range(board.board_size) for c in range(board.board_size)]
        print(board)

    #  if the location is not a bomb, dig recursively until each square is at least next to a bomb
    #  repeat until there are no places left to dig


if __name__ == '__main__':
    play()
