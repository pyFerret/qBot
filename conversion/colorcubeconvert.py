# this may take the longest of these files,
# but I plan to use it to convert colors of the 
# stickers to the virtual cube pieces and vice versa. 
# I am not looking forward to this lmao

import png
from conversion.binaryTranslation.bincubeconvert import *


class ColorConverter:
    def __init__(self, cube=form_cube(_sorted=True)):
        self.img = png.Writer(width=12, height=9, greyscale=False)
        
        self.black = [0, 0,  0]
        self.red = [255, 0, 0]
        self.green = [0, 255, 0]
        self.blue = [0, 0, 255]
        self.orange = [255, 127, 0]
        self.yellow = [225, 225, 0]
        self.white = [255, 255, 255]
        
        self.piece_colors = {
            'a': [self.white,  self.orange, self.blue],
            'b': [self.white,  self.blue],
            'c': [self.white,  self.blue,   self.red],
            'd': [self.white,  self.orange],
            'e': [self.white],
            'f': [self.white,  self.red],
            'g': [self.white,  self.green,  self.orange],
            'h': [self.white,  self.green],
            'i': [self.white,  self.red,    self.green],
            'j': [self.blue,   self.orange],
            'k': [self.blue],
            'l': [self.blue,   self.red],
            'm': [self.orange],
            'n': [self.red],
            'o': [self.green,  self.orange],
            'p': [self.green],
            'q': [self.green,  self.red],
            'r': [self.yellow, self.blue,   self.orange],
            's': [self.yellow, self.blue],
            't': [self.yellow, self.red,    self.blue],
            'u': [self.yellow, self.orange],
            'v': [self.yellow],
            'w': [self.yellow, self.red],
            'x': [self.yellow, self.orange, self.green],
            'y': [self.yellow, self.green],
            'z': [self.yellow, self.green,  self.red]
        }
        
        self.cube_colors = []
        
        self.cube = cube
        
        self.initialize()
        self.draw_cube(self.cube)
        self.create()

    def draw(self, i, a, color):
        self.cube_colors[i][a * 3 + 0] = color[0]
        self.cube_colors[i][a * 3 + 1] = color[1]
        self.cube_colors[i][a * 3 + 2] = color[2]

    def initialize(self):
        self.cube_colors = []
        for i in range(9):
            self.cube_colors.append([])
            for a in range(36):
                self.cube_colors[i].append([])
        for i in range(9):
            for a in range(12):
                self.draw(i, a, self.black)

    def draw_cube(self, c):
        for i in c:
            if c[i][1] == 1:
                self.draw(0, 3, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(3, 0, self.piece_colors[i][(c[i][0] + 0) % 3])
                self.draw(3, 11, self.piece_colors[i][(c[i][0] + 1) % 3])
            elif c[i][1] == 2:
                self.draw(0, 4, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(3, 10, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 3:
                self.draw(0, 5, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(3, 9, self.piece_colors[i][(c[i][0] + 0) % 3])
                self.draw(3, 8, self.piece_colors[i][(c[i][0] + 1) % 3])
            elif c[i][1] == 4:
                self.draw(1, 3, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(3, 1, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 5:
                self.draw(1, 4, self.piece_colors[i][0])
            elif c[i][1] == 6:
                self.draw(1, 5, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(3, 7, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 7:
                self.draw(2, 3, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(3, 2, self.piece_colors[i][(c[i][0] + 1) % 3])
                self.draw(3, 3, self.piece_colors[i][(c[i][0] + 0) % 3])
            elif c[i][1] == 8:
                self.draw(2, 4, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(3, 4, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 9:
                self.draw(2, 5, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(3, 5, self.piece_colors[i][(c[i][0] + 1) % 3])
                self.draw(3, 6, self.piece_colors[i][(c[i][0] + 0) % 3])
            elif c[i][1] == 10:
                self.draw(4, 0, self.piece_colors[i][(c[i][0] - 0) % 2])
                self.draw(4, 11, self.piece_colors[i][(c[i][0] - 1) % 2])
            elif c[i][1] == 11:
                self.draw(4, 10, self.piece_colors[i][0])
            elif c[i][1] == 12:
                self.draw(4, 9, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(4, 8, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 13:
                self.draw(4, 1, self.piece_colors[i][0])
            elif c[i][1] == 14:
                self.draw(4, 7, self.piece_colors[i][0])
            elif c[i][1] == 15:
                self.draw(4, 2, self.piece_colors[i][(c[i][0] - 0) % 2])
                self.draw(4, 3, self.piece_colors[i][(c[i][0] - 1) % 2])
            elif c[i][1] == 16:
                self.draw(4, 4, self.piece_colors[i][0])
            elif c[i][1] == 17:
                self.draw(4, 5, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(4, 6, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 18:
                self.draw(6, 3, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(5, 0, self.piece_colors[i][(c[i][0] + 1) % 3])
                self.draw(5, 11, self.piece_colors[i][(c[i][0] + 0) % 3])
            elif c[i][1] == 19:
                self.draw(6, 4, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(5, 10, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 20:
                self.draw(6, 5, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(5, 9, self.piece_colors[i][(c[i][0] + 1) % 3])
                self.draw(5, 8, self.piece_colors[i][(c[i][0] + 0) % 3])
            elif c[i][1] == 21:
                self.draw(7, 3, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(5, 1, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 22:
                self.draw(7, 4, self.piece_colors[i][0])
            elif c[i][1] == 23:
                self.draw(7, 5, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(5, 7, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 24:
                self.draw(8, 3, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(5, 2, self.piece_colors[i][(c[i][0] + 0) % 3])
                self.draw(5, 3, self.piece_colors[i][(c[i][0] + 1) % 3])
            elif c[i][1] == 25:
                self.draw(8, 4, self.piece_colors[i][(c[i][0] - 1) % 2])
                self.draw(5, 4, self.piece_colors[i][(c[i][0] - 0) % 2])
            elif c[i][1] == 26:
                self.draw(8, 5, self.piece_colors[i][(c[i][0] - 1) % 3])
                self.draw(5, 5, self.piece_colors[i][(c[i][0] + 0) % 3])
                self.draw(5, 6, self.piece_colors[i][(c[i][0] + 1) % 3])
            else:
                pass

    def create(self): 
        with open("assets/visualizer/cubevis.png", "wb") as file:
            self.img.write(file, self.cube_colors)
    
    def update(self):
        self.draw_cube(self.cube)
        self.create()
