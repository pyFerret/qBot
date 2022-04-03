# this may take the longest of any of these files,
# but I plan to use it to convert colors of the 
# stickers to the virtual cube pieces and vice versa. 
# i am not looking forward to this lmao

import png

class colorconverter:
    def __init__():
        img = png.Writer(width=12, height=9, greyscale=False)
        
        black =  [0,   0,   0]
        red =    [255, 0,   0]
        green =  [0,   255, 0]
        blue =   [0,   0,   255]
        orange = [255, 127, 0]
        yellow = [225, 225, 0]
        white =  [255, 255, 255]
        
        cubecolors = []

    def draw(self, i, a, color):
        self.cubecolors[i][a*3+0] = color[0]
        self.cubecolors[i][a*3+1] = color[1]
        self.cubecolors[i][a*3+2] = color[2]

    def initialize(self):
        cubecolors = []
        for i in range(9):
            cubecolors.append([])
            for a in range(36):
                cubecolors[i].append([])
        for i in range(9):
            for a in range(12):
                self.draw(i, a, self.black)

    def create(self): 
        with open("cubevis.png", "wb") as file: self.img.write(file, self.cubecolors)
