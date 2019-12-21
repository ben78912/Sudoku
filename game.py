from sudoku import complete, can_place, empty
import pygame

width = 360
height = 360
square_size = width // 3
cell_size = square_size // 3

black = (0, 0, 0)
white = (255,255,255)
grey = (192, 192, 192)

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
    pygame.display.set_caption('Sudoku')

    global font, small_font
    font = pygame.font.Font('freesansbold.ttf', font_size)
    small_font = pygame.font.Font('freesansbold.ttf', font_small)

    update_display()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(board, 0, 0)
                    break
        
        # gameDisplay.fill(white)
        # draw_grid(gameDisplay)
        # populate_grid(playing_board, gameDisplay)

        pygame.display.update()

def update_display():
    gameDisplay.fill(white)
    draw_grid(gameDisplay)
    populate_grid(board, gameDisplay)
    pygame.display.update()
    pygame.time.delay(50)


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



if __name__=='__main__':
    main()