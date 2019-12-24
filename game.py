from sudoku import complete, can_place, empty
from numpy import floor
from itertools import product
import pygame

width = 360
height = 360
square_size = width // 3
cell_size = square_size // 3

black = (0, 0, 0)
white = (255,255,255)
grey = (192, 192, 192)
red = (255, 0, 0)

font_size = 44
font_small = font_size // 2

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

playing_board = board[:]

def main():
    pygame.init()
    global gameDisplay
    gameDisplay = pygame.display.set_mode((width, height))
    mouseClicked = False
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Sudoku')

    global font, small_font
    font = pygame.font.Font('freesansbold.ttf', font_size)
    small_font = pygame.font.Font('freesansbold.ttf', font_small)

    update_display()

    while True:
        key = 0
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(board, 0, 0)
                elif event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9
                elif event.key == pygame.K_BACKSPACE:
                    key = 0
                    draw_number(mousex, mousey, key)
                elif event.key == pygame.K_RETURN:
                    if validate_board(board):
                        print("Game Over")
            
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        
        if mouseClicked:
            update_display()
            box_x = int(cell_size * floor(mousex / cell_size))
            box_y = int(cell_size * floor(mousey / cell_size))

            draw_selected(box_x, box_y)

        if key != 0:
            draw_number(mousex, mousey, key)

def update_display():
    gameDisplay.fill(white)
    draw_grid(gameDisplay)
    populate_grid(board, gameDisplay)
    pygame.display.update()
    pygame.time.delay(50)

def draw_number(x, y, num):
    row = int(floor(y // cell_size))
    column = int(floor(x / cell_size))

    board[row][column] = num
    update_display()
    
def draw_selected(x, y):
    pygame.draw.rect(gameDisplay, red, (x, y, cell_size, cell_size), 1)
    pygame.display.update()


def solve(board, row, col):
    if col == len(board):
        col = 0
        row += 1

        if row == len(board):
            return True

    if board[row][col] != empty:
        return solve(board, row, col + 1)
    # Place from 1 - 9 in the grid
    for value in range(1, 10):
        if can_place(board, row, col, value): 
            board[row][col] = value
            update_display()
            if solve(board, row, col + 1):
                return True
        
            # Back track because the placement broke the board
            board[row][col] = 0
            update_display()
        
    # Board was broken
    return False

def draw_grid(gameDisplay):
    # Cell lines
    for i in range(0, width, cell_size):
        pygame.draw.line(gameDisplay, grey, (i, 0), (i, height))
    
    for i in range(0, height, cell_size):
        pygame.draw.line(gameDisplay, grey, (0, i), (width, i))

    # Square grid border lines
    for i in range(0, width, square_size):
        pygame.draw.line(gameDisplay, black, (i, 0), (i, height))
    
    for i in range(0, height, square_size):
        pygame.draw.line(gameDisplay, black, (0, i), (width, i))

def populate_grid(board, gameDisplay):
    x_offset = cell_size // 4
    y_offset = 0
    for row in board:
        for i in row:
            if i != empty:
                draw_cell(gameDisplay, x_offset, y_offset, i)
            x_offset += 40
            if x_offset > 360:
                x_offset = cell_size // 4
        y_offset += 40 


# Draw cell at 
def draw_cell(gameDisplay, x, y, num):
    cell = font.render('%s' %num, True, grey)
    rect = cell.get_rect()
    rect.topleft = (x, y)
    gameDisplay.blit(cell, rect)


def validate_board(board):
    
    for row in board:
        if 0 in set(row):
            print('Board incomplete')
            return False
    
    DIGITS = set(range(1, 10))

    # Check rows
    for i in range(len(board)):
        if not set(board[i]) == DIGITS:
            print('Row %s contains a duplicate number' %(i + 1))
            return False

    # Check columns
    columns = [[row[c] for row in board] for c in range(9)]
    for i in range(len(columns)):
        if not set(columns[i]) == DIGITS:
            print('Column %s contains a duplicate number' %(i + 1))
            return False
    
    THREES  = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    grid = 1
    for row_block, col_block in product(THREES, THREES):
        pairs = list(product(row_block, col_block))
        block = []
        for i in range(len(pairs)):
            block.append(board[pairs[i][0]][pairs[i][1]])

        
        if not set(block) == DIGITS:
            print('Grid %s contains a duplicate' %grid)
            grid += 1
            return False

    return True


if __name__=='__main__':
    main()