from tile import Tile


class Entanglement:

    SIZE = 7 # must be odd

    board = None
    pos_row = None
    pos_col = None
    score = None

    def __init__(self):
        self._init_board()

        self.pos_row = self.SIZE//2
        self.pos_col = self.SIZE//2 + 1
        self.start_direction = 5 # down left

        self.score = 0

        self.new_tile = Tile()
        self.alternate_tile = Tile()

    
    def _init_board(self):
        self.board = []

        self.board.append([False for _ in range(self.SIZE + 2)])
        for _ in range(self.SIZE):
            self.board.append([False] + [None for _ in range(self.SIZE)] + [False])
        self.board.append([False for _ in range(self.SIZE + 2)])
        
        self.board[self.SIZE//2 + 1][self.SIZE//2 + 1] = False # center

    

    def rotate_tile_cw(self):
        self.new_tile.rotate_cw()

    def rotate_tile_ccw(self):
        self.new_tile.rotate_ccw()
    
    def swap_tile(self):
        self.new_tile, self.alternate_tile = self.alternate_tile, self.new_tile



    def _get_next_tile(self, row, col, start_direction):
        end_direction = self.board[row][col].line[start_direction]
        dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][end_direction // 2]

        return row+dr, col+dc, [5,4,7,6,1,0,3,2][end_direction]
    
    def _is_alive(self):
        if self.pos_row == self.pos_col == self.SIZE // 2 + 1:
            return False
        
        return 1 <= self.pos_row <= self.SIZE and 1 <= self.pos_col <= self.SIZE

    
    # follow path and calculate score by this move
    def _follow_path(self):
        count = 1
        current_tile = self.board[self.pos_row][self.pos_col]
        current_tile.passed.append((self.start_direction, current_tile.line[self.start_direction]))
        next_row, next_col, next_start_direction = self._get_next_tile(self.pos_row, self.pos_col, self.start_direction)

        while self.board[next_row][next_col]: # loop until no tile or dead
            count += 1
            current_tile = self.board[next_row][next_col]
            current_tile.passed.append((next_start_direction, current_tile.line[next_start_direction]))
            next_row, next_col, next_start_direction = self._get_next_tile(next_row, next_col, next_start_direction)
        
        self.pos_row = next_row
        self.pos_col = next_col
        self.start_direction = next_start_direction

        self.score += count * (count + 1) // 2


    def put_tile(self):
        self.board[self.pos_row][self.pos_col] = self.new_tile
        self._follow_path()
        # print("Score:", self.score)

        self.new_tile = Tile()
        self.alternate_tile = Tile()
        self.tile_chosen = 0

        return self._is_alive()