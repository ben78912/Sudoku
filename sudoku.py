from numpy import sqrt

empty = 0
board = [[1, 0, 0, 0, 0, 6, 0, 0, 4],
         [0, 0, 5, 0, 0, 0, 1, 8, 0],
         [0, 0, 3, 8, 7, 0, 2, 9, 0],
         [0, 0, 0, 0, 0, 9, 0, 0, 0],
         [6, 0, 7, 0, 4, 0, 9, 0, 2],
         [0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 6, 0, 9, 2, 5, 0, 0],
         [0, 2, 8, 0, 0, 0, 7, 0, 0],
         [3, 0, 0, 5, 0, 0, 0, 0, 1]
         ]


def complete(board, row, col):
    if col == len(board):
        col = 0
        row += 1

        if row == len(board):
            return True

    if board[row][col] != empty:
        return complete(board, row, col + 1)
    # Place from 1 - 9 in the grid
    for value in range(1, 10):
        if can_place(board, row, col, value): 
            board[row][col] = value
            if complete(board, row, col + 1):
                return True
        
            # Back track because the placement broke the board
            board[row][col] = 0
        
    # Board was broken
    return False

def can_place(board, row, col, char):

    for i in range(len(board)):
        # Check if the row is valid
        if board[row][i] == char:
            return False

    for i in range(len(board)):
        # Check if the column is valid
        if board[i][col] == char:
            return False
    
    # Check if sub Box is valid
    # Get regions of box
    sub_box_size = int(sqrt(len(board)))
    horizontal_index =  row // sub_box_size
    vertical_index = col // sub_box_size

    top_left_col = vertical_index * sub_box_size
    top_left_row = horizontal_index * sub_box_size

    for i in range(top_left_row, top_left_row + 3):
        for j in range(top_left_col, top_left_col + 3):
            if board[i][j] == char:
                return False
    return True


def print_rows(board):
    for row in board:
        print(row)
        print("---------------------------")

def main():
    print_rows(board)
    complete(board, 0, 0)
    print('\n')
    print_rows(board)


if __name__=='__main__':
    main()
