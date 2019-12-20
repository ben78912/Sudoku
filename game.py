from sudoku import complete, empty
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

board = [[0, 0, 0, 0, 0, 0, 0, 5, 0],
         [0, 2, 0, 0, 7, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 6, 0, 9, 3],
         [6, 7, 4, 8, 0, 0, 0, 0, 9],
         [0, 0, 0, 3, 0, 4, 0, 0, 0],
         [3, 0, 0, 0, 0, 7, 8, 4, 5],
         [4, 8, 0, 2, 0, 0, 0, 0, 0],
         [9, 0, 0, 0, 5, 0, 0, 1, 0],
         [0, 6, 0, 0, 0, 0, 0, 0, 0]
         ]

def main():
    pygame.init()
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sudoku')

    global font, small_font
    font = pygame.font.Font('freesansbold.ttf', font_size)
    small_font = pygame.font.Font('freesansbold.ttf', font_small)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        draw_grid(gameDisplay)
        populate_grid(gameDisplay)

        pygame.display.update()
        clock.tick(60)


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

def populate_grid(gameDisplay):
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