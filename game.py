import sys
import pygame as pg
from pygame.locals import *
from entanglement import Entanglement


# screen
W = 900
H = 720
fps = 10

# colors
BLACK  = (  0,  0,  0)
LIGHT_GREY = (200,200,200)
GREY   = (100,100,100)
WHITE  = (255,255,255)
RED    = (255,0,0)

entanglement = Entanglement()

SIZE = 90 # should be a multiple of 3
BASE_X = 30
BASE_Y = 45

PATH_POS_OFFSET = [
    (SIZE//3, 0), (SIZE//3 * 2, 0),       # 0, 1
    (SIZE, SIZE//3), (SIZE, SIZE//3 * 2), # 2, 3
    (SIZE//3 * 2, SIZE), (SIZE//3, SIZE), # 4, 5
    (0, SIZE//3 * 2), (0, SIZE//3)        # 6, 7
]

SWAP_AREA_SIZE = SIZE * 2
SWAP_AREA_BASE = (690, 495)




def draw_tile(screen, tile, row, col):
    if not tile:
        return
    
    tile_base_x = BASE_X + col * SIZE
    tile_base_y = BASE_Y + row * SIZE

    pg.draw.rect(screen, GREY, (tile_base_x, tile_base_y, SIZE, SIZE))

    for start in range(8):
        end = tile.line[start]
        start_pos = (tile_base_x + PATH_POS_OFFSET[start][0], tile_base_y + PATH_POS_OFFSET[start][1])
        end_pos = (tile_base_x + PATH_POS_OFFSET[end][0], tile_base_y + PATH_POS_OFFSET[end][1])
        pg.draw.line(screen, WHITE, start_pos, end_pos, width=5)

    for start, end in tile.passed:
        start_pos = (tile_base_x + PATH_POS_OFFSET[start][0], tile_base_y + PATH_POS_OFFSET[start][1])
        end_pos = (tile_base_x + PATH_POS_OFFSET[end][0], tile_base_y + PATH_POS_OFFSET[end][1])
        pg.draw.line(screen, RED, start_pos, end_pos, width=5)





border_lines = []
for i in range(entanglement.SIZE+1):
    border_lines.append(((BASE_X, BASE_Y + i*SIZE), (BASE_X + entanglement.SIZE*SIZE, BASE_Y + i*SIZE)))
    border_lines.append(((BASE_X + i*SIZE, BASE_Y), (BASE_X + i*SIZE, BASE_Y + entanglement.SIZE*SIZE)))


pg.init()
pg.display.set_caption("Entanglement")
screen = pg.display.set_mode((W, H), 0, 32)
clock = pg.time.Clock()
playing = True

font_small = pg.font.SysFont("consolas", 30, True, False)
font_large = pg.font.SysFont("consolas", 60, True, False)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_r:
                playing = True
                entanglement.__init__()

            if not playing:
                # print("you are dead!")
                break

            if event.key == K_RETURN:
                playing = entanglement.put_tile()
            if event.key == K_LEFT:
                entanglement.rotate_tile_ccw()
            if event.key == K_RIGHT:
                entanglement.rotate_tile_cw()
            if event.key == K_SPACE:
                entanglement.swap_tile()


    
    screen.fill(LIGHT_GREY)

    # draw tiles
    for row in range(1, entanglement.SIZE+1):
        for col in range(1, entanglement.SIZE+1):
            draw_tile(screen, entanglement.board[row][col], row-1, col-1)

    # draw lines
    for start, end in border_lines:
        pg.draw.line(screen, BLACK, start, end, width=2)

    # draw center
    pg.draw.rect(screen, BLACK, (BASE_X + entanglement.SIZE//2 * SIZE, BASE_Y + entanglement.SIZE//2 * SIZE, SIZE, SIZE))

    # draw current tile
    if playing:
        new_tile = entanglement.new_tile
        current_row = entanglement.pos_row
        current_col = entanglement.pos_col
        draw_tile(screen, new_tile, current_row-1, current_col-1)

    # score area
    score_text = font_small.render("SCORE:" if playing else "DEAD!", True, BLACK)
    screen.blit(score_text, (675,100))
    score_text = font_large.render(str(entanglement.score), True, BLACK)
    screen.blit(score_text, (780,80))

    # draw swap area
    if playing:
        pg.draw.rect(screen, GREY, SWAP_AREA_BASE + (SWAP_AREA_SIZE, SWAP_AREA_SIZE))
        alternate_tile = entanglement.alternate_tile
        for start in range(8):
            end = alternate_tile.line[start]
            start_pos = (SWAP_AREA_BASE[0] + 2*PATH_POS_OFFSET[start][0], SWAP_AREA_BASE[1] + 2*PATH_POS_OFFSET[start][1])
            end_pos = (SWAP_AREA_BASE[0] + 2*PATH_POS_OFFSET[end][0], SWAP_AREA_BASE[1] + 2*PATH_POS_OFFSET[end][1])
            pg.draw.line(screen, WHITE, start_pos, end_pos, width=5)


    pg.display.update()
    clock.tick(fps)