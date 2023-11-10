from random import shuffle

class Tile:
    base = [0,1,2,3,4,5,6,7]

    def __init__(self):
        shuffle(self.base)

        self.pair = [[self.base[i], self.base[i+4], False] for i in range(4)] # (dot A, dot B, is passed)
        self.line = [None] * 8
        for i,(start,end,_) in enumerate(self.pair): # i: to know the what order the line is
            self.line[start] = [end, i]
            self.line[end] = [start, i]

    def rotate_cw(self):
        for line in self.pair:
            line[0],line[1] = (line[0]+2) % 8,(line[1]+2) % 8
        self.line[0][0],self.line[1][0],self.line[2][0],self.line[3][0],self.line[4][0],self.line[5][0],self.line[6][0],self.line[7][0] = (self.line[6][0]+2) % 8, (self.line[7][0]+2) % 8, (self.line[0][0]+2) % 8, (self.line[1][0]+2) % 8, (self.line[2][0]+2) % 8, (self.line[3][0]+2) % 8, (self.line[4][0]+2) % 8, (self.line[5][0]+2) % 8
        self.line[0][1],self.line[1][1],self.line[2][1],self.line[3][1],self.line[4][1],self.line[5][1],self.line[6][1],self.line[7][1] = self.line[6][1], self.line[7][1], self.line[0][1], self.line[1][1], self.line[2][1], self.line[3][1], self.line[4][1], self.line[5][1]

    def rotate_ccw(self):
        for line in self.pair:
            line[0],line[1] = (line[0]-2) % 8, (line[1]-2) % 8
        self.line[0][0],self.line[1][0],self.line[2][0],self.line[3][0],self.line[4][0],self.line[5][0],self.line[6][0],self.line[7][0] = (self.line[2][0]-2) % 8, (self.line[3][0]-2) % 8, (self.line[4][0]-2) % 8, (self.line[5][0]-2) % 8, (self.line[6][0]-2) % 8, (self.line[7][0]-2) % 8, (self.line[0][0]-2) % 8, (self.line[1][0]-2) % 8
        self.line[0][1],self.line[1][1],self.line[2][1],self.line[3][1],self.line[4][1],self.line[5][1],self.line[6][1],self.line[7][1] = self.line[2][1], self.line[3][1], self.line[4][1], self.line[5][1], self.line[6][1], self.line[7][1], self.line[0][1], self.line[1][1]