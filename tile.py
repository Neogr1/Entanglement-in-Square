from random import shuffle

class Tile:
    base = [0,1,2,3,4,5,6,7]

    def __init__(self):
        shuffle(self.base)
        pair = [(self.base[i], self.base[i+4]) for i in range(4)]

        self.line = [None] * 8
        self.passed = []
        for a,b in pair:
            self.line[a] = b
            self.line[b] = a

    def rotate_cw(self):
        self.line[0],self.line[1],self.line[2],self.line[3],self.line[4],self.line[5],self.line[6],self.line[7] = (self.line[6]+2) % 8, (self.line[7]+2) % 8, (self.line[0]+2) % 8, (self.line[1]+2) % 8, (self.line[2]+2) % 8, (self.line[3]+2) % 8, (self.line[4]+2) % 8, (self.line[5]+2) % 8

    def rotate_ccw(self):
        self.line[0],self.line[1],self.line[2],self.line[3],self.line[4],self.line[5],self.line[6],self.line[7] = (self.line[2]-2) % 8, (self.line[3]-2) % 8, (self.line[4]-2) % 8, (self.line[5]-2) % 8, (self.line[6]-2) % 8, (self.line[7]-2) % 8, (self.line[0]-2) % 8, (self.line[1]-2) % 8