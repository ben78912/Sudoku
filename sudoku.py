from numpy import sqrt

rows = [[0, 0, 9, 0, 0, 0, 8, 0, 2],
        [0, 0, 0, 4, 7, 0, 0, 0, 9],
        [1, 5, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 1, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 6],
        [6, 0, 0, 0, 1, 5, 0, 0, 0],
        [9, 0, 5, 0, 0, 0, 3, 0, 0]
        ]


def complete(row, col):
    if col == len(rows):
        col = 0
        row += 1

        if row == len(rows):
            return True

    if rows[row][col] != 0:
        return complete(row, col + 1)
    # Place from 1 - 9 in the grid
    for value in range(1, 10):
        if can_place(row, col, value): 
            rows[row][col] = value
            if complete(row, col + 1):
                return True
        
            # Back track because the placement broke the board
            rows[row][col] = 0
        
    # Board was broken
    return False

def can_place(row, col, char):

    for i in range(len(rows)):
        # Check if the row is valid
        if rows[row][i] == char:
            return False

        # Check if the column is valid
        if rows[i][col] == char:
            return False
    
    # Check if sub Box is valid
    # Get regions of box
    sub_box_size = int(sqrt(len(rows)))
    horizontal_index =  row // sub_box_size
    vertical_index = col // sub_box_size

    top_left_col = vertical_index * sub_box_size
    top_left_row = horizontal_index * sub_box_size

    for i in range(top_left_row, top_left_row + 3):
        for j in range(top_left_col, top_left_col + 3):
            if rows[i][j] == char:
                return False
    return True


def print_rows(rows):
    for row in rows:
        print(row)
        print("---------------------------")


print_rows(rows)
complete(0, 0)
print("\n")
print("\n")
print_rows(rows)
