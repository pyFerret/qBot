import binaryTranslation.bincubeconvert as bcc

# This file contains the class that I use to dictate what a cube is
# If you would like a new cube you can just make one with this class

class Cube():
    
    # the virtual cube, in most files that it is accessed, 
    # is held with the Green side facing and the White side 
    # up. comments from this point on will be based on that.
    
    def __init__(self, sort, scramble):
        self.cube = bcc.formCube(sort, scramble) # this is the actual virtual cube. 
                                                 # the rest of the file is manipulation 
                                                 # of said actual virtual cube
        self.nRL = ["b", "h", "s", "y"] # nRL stands for Not Right or Left
        self.nUD = ["j", "l", "o", "q"] # nUD stands for Not Up or Down
        self.nFB = ["d", "f", "u", "w"] # nFB stands for Not Front or Back
        # these three lists are used as lists of the edges not found on two opposite sides (like not right or left side edges)
    
    def pieceChange(self, p, x): # this will basically change where a piece is.
        self.cube[p][1] = x      # its probably not the best way to do it but i dont really care

    def oriCorner(self, p, w): # this will change the orientation of a corner
        self.cube[p][0] = self.CornerOCW(self.cube[p][0]) if w == "OCW" else self.CornerOCCW(self.cube[p][0])
    
    def oriEdge(self, p, s): # this will change the orientation of an edge
        self.cube[p][0] = self.edgeCheck(s, self.cube[p][0], p)
    
    def R(self, _inverted = False): # this function will turn the right (red) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (R -> R')
            for i in self.cube: # im looking at this now and i feel like these two lines
                i = str(i)      # could be a lot better if i didnt do the second one, 
                                # and instead made it a separate variable. i think i
                                # will change it in the future but i dont have time rn
    
                piece = self.cube[i][1] # the location of the piece being dealt with currently
    
                if piece == 9: # the next four ifs move the corners around the right side
                    self.pieceChange(i, 26)
                    self.oriCorner(i, "OCW")
                elif piece == 3:
                    self.pieceChange(i, 9)
                    self.oriCorner(i, "OCCW")
                elif piece == 20:
                    self.pieceChange(i, 3)
                    self.oriCorner(i, "OCW")
                elif piece == 26:
                    self.pieceChange(i, 20)
                    self.oriCorner(i, "OCCW")
                elif piece == 6: # the next four ifs move the edges around the right side
                    self.pieceChange(i, 17)
                    self.oriEdge(i, "R")
                elif piece == 12:
                    self.pieceChange(i, 6)
                    self.oriEdge(i, "R")
                elif piece == 23:
                    self.pieceChange(i, 12)
                    self.oriEdge(i, "R")
                elif piece == 17:
                    self.pieceChange(i, 23)
                    self.oriEdge(i, "R")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9: # the next four ifs move the corners around the right side
                    self.pieceChange(i, 3)
                    self.oriCorner(i, "OCW")
                elif piece == 3:
                    self.pieceChange(i, 20)
                    self.oriCorner(i, "OCCW")
                elif piece == 20:
                    self.pieceChange(i, 26)
                    self.oriCorner(i, "OCW")
                elif piece == 26:
                    self.pieceChange(i, 9)
                    self.oriCorner(i, "OCCW")
                elif piece == 6: # the next four ifs move the edges around the right side
                    self.pieceChange(i, 12)
                    self.oriEdge(i, "R")
                elif piece == 12:
                    self.pieceChange(i, 23)
                    self.oriEdge(i, "R")
                elif piece == 23:
                    self.pieceChange(i, 17)
                    self.oriEdge(i, "R")
                elif piece == 17:
                    self.pieceChange(i, 6)
                    self.oriEdge(i, "R")
    
    def L(self, _inverted = False): # this function will turn the left (orange) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (L -> L')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    self.pieceChange(i, 18)
                    self.oriCorner(i, "OCW")
                elif piece == 18:
                    self.pieceChange(i, 24)
                    self.oriCorner(i, "OCCW")
                elif piece == 24:
                    self.pieceChange(i, 7)
                    self.oriCorner(i, "OCW")
                elif piece == 7:
                    self.pieceChange(i, 1)
                    self.oriCorner(i, "OCCW")
                elif piece == 4:
                    self.pieceChange(i, 10)
                    self.oriEdge(i, "L")
                elif piece == 10:
                    self.pieceChange(i, 21)
                    self.oriEdge(i, "L")
                elif piece == 21:
                    self.pieceChange(i, 15)
                    self.oriEdge(i, "L")
                elif piece == 15:
                    self.pieceChange(i, 4)
                    self.oriEdge(i, "L")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    self.pieceChange(i, 7)
                    self.oriCorner(i, "OCW")
                elif piece == 7:
                    self.pieceChange(i, 24)
                    self.oriCorner(i, "OCCW")
                elif piece == 24:
                    self.pieceChange(i, 18)
                    self.oriCorner(i, "OCW")
                elif piece == 18:
                    self.pieceChange(i, 1)
                    self.oriCorner(i, "OCCW")
                elif piece == 4:
                    self.pieceChange(i, 15)
                    self.oriEdge(i, "L")
                elif piece == 15:
                    self.pieceChange(i, 21)
                    self.oriEdge(i, "L")
                elif piece == 21:
                    self.pieceChange(i, 10)
                    self.oriEdge(i, "L")
                elif piece == 10:
                    self.pieceChange(i, 4)
                    self.oriEdge(i, "L")
    
    def U(self, _inverted = False): # this function will turn the up (white) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (U -> U')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    self.pieceChange(i, 3)
                elif piece == 3:
                    self.pieceChange(i, 1)
                elif piece == 1:
                    self.pieceChange(i, 7)
                elif piece == 7:
                    self.pieceChange(i, 9)
                elif piece == 6:
                    self.pieceChange(i, 2)
                    self.oriEdge(i, "U")
                elif piece == 2:
                    self.pieceChange(i, 4)
                    self.oriEdge(i, "U")
                elif piece == 4:
                    self.pieceChange(i, 8)
                    self.oriEdge(i, "U")
                elif piece == 8:
                    self.pieceChange(i, 6)
                    self.oriEdge(i, "U")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    self.pieceChange(i, 7)
                elif piece == 7:
                    self.pieceChange(i, 1)
                elif piece == 1:
                    self.pieceChange(i, 3)
                elif piece == 3:
                    self.pieceChange(i, 9)
                elif piece == 6:
                    self.pieceChange(i, 8)
                    self.oriEdge(i, "U")
                elif piece == 8:
                    self.pieceChange(i, 4)
                    self.oriEdge(i, "U")
                elif piece == 4:
                    self.pieceChange(i, 2)
                    self.oriEdge(i, "U")
                elif piece == 2:
                    self.pieceChange(i, 6)
                    self.oriEdge(i, "U")
    
    def D(self, _inverted = False): # this function will turn the down (yellow) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (D -> D')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 18:
                    self.pieceChange(i, 20)
                elif piece == 20:
                    self.pieceChange(i, 26)
                elif piece == 26:
                    self.pieceChange(i, 24)
                elif piece == 24:
                    self.pieceChange(i, 18)
                elif piece == 19:
                    self.pieceChange(i, 23)
                    self.oriEdge(i, "D")
                elif piece == 23:
                    self.pieceChange(i, 25)
                    self.oriEdge(i, "D")
                elif piece == 25:
                    self.pieceChange(i, 21)
                    self.oriEdge(i, "D")
                elif piece == 21:
                    self.pieceChange(i, 19)
                    self.oriEdge(i, "D")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 18:
                    self.pieceChange(i, 24)
                elif piece == 24:
                    self.pieceChange(i, 26)
                elif piece == 26:
                    self.pieceChange(i, 20)
                elif piece == 20:
                    self.pieceChange(i, 18)
                elif piece == 19:
                    self.pieceChange(i, 21)
                    self.oriEdge(i, "D")
                elif piece == 21:
                    self.pieceChange(i, 25)
                    self.oriEdge(i, "D")
                elif piece == 25:
                    self.pieceChange(i, 23)
                    self.oriEdge(i, "D")
                elif piece == 23:
                    self.pieceChange(i, 19 )
                    self.oriEdge(i, "D")
    
    def F(self, _inverted = False): # this function will turn the front (green) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (F -> F')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    self.pieceChange(i, 7)
                    self.oriCorner(i, "OCCW")
                elif piece == 7:
                    self.pieceChange(i, 24)
                    self.oriCorner(i, "OCW")
                elif piece == 24:
                    self.pieceChange(i, 26)
                    self.oriCorner(i, "OCCW")
                elif piece == 26:
                    self.pieceChange(i, 9)
                    self.oriCorner(i, "OCW")
                elif piece == 8:
                    self.pieceChange(i, 15)
                    self.oriEdge(i, "F")
                elif piece == 15:
                    self.pieceChange(i, 25)
                    self.oriEdge(i, "F")
                elif piece == 25:
                    self.pieceChange(i, 17)
                    self.oriEdge(i, "F")
                elif piece == 17:
                    self.pieceChange(i, 8)
                    self.oriEdge(i, "F")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    self.pieceChange(i, 26)
                    self.oriCorner(i, "OCCW")
                elif piece == 26:
                    self.pieceChange(i, 24)
                    self.oriCorner(i, "OCW")
                elif piece == 24:
                    self.pieceChange(i, 7)
                    self.oriCorner(i, "OCCW")
                elif piece == 7:
                    self.pieceChange(i, 9)
                    self.oriCorner(i, "OCW")
                elif piece == 8:
                    self.pieceChange(i, 17)
                    self.oriEdge(i, "F")
                elif piece == 17:
                    self.pieceChange(i, 25)
                    self.oriEdge(i, "F")
                elif piece == 25:
                    self.pieceChange(i, 15)
                    self.oriEdge(i, "F")
                elif piece == 15:
                    self.pieceChange(i, 8)
                    self.oriEdge(i, "F")
    
    def B(self, _inverted = False): # this function will turn the back (blue) side clockwise (unless inverted is true)
        if _inverted: # if its inverted it will do the inverse move (B -> B')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    self.pieceChange(i, 3)
                    self.oriCorner(i, "OCCW")
                elif piece == 3:
                    self.pieceChange(i, 20)
                    self.oriCorner(i, "OCW")
                elif piece == 20:
                    self.pieceChange(i, 18)
                    self.oriCorner(i, "OCCW")
                elif piece == 18:
                    self.pieceChange(i, 1)
                    self.oriCorner(i, "OCW")
                elif piece == 2:
                    self.pieceChange(i, 12)
                    self.oriEdge(i, "B")
                elif piece == 12:
                    self.pieceChange(i, 19)
                    self.oriEdge(i, "B")
                elif piece == 19:
                    self.pieceChange(i, 10)
                    self.oriEdge(i, "B")
                elif piece == 10:
                    self.pieceChange(i, 2)
                    self.oriEdge(i, "B")
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    self.pieceChange(i, 18)
                    self.oriCorner(i, "OCCW")
                elif piece == 18:
                    self.pieceChange(i, 20)
                    self.oriCorner(i, "OCW")
                elif piece == 20:
                    self.pieceChange(i, 3)
                    self.oriCorner(i, "OCCW")
                elif piece == 3:
                    self.pieceChange(i, 1)
                    self.oriCorner(i, "OCW")
                elif piece == 2:
                    self.pieceChange(i, 10)
                    self.oriEdge(i, "B")
                elif piece == 10:
                    self.pieceChange(i, 19)
                    self.oriEdge(i, "B")
                elif piece == 19:
                    self.pieceChange(i, 12)
                    self.oriEdge(i, "B")
                elif piece == 12:
                    self.pieceChange(i, 2)
                    self.oriEdge(i, "B")
    
    def CornerOCCW(self, _co):
        _co-=1
        if _co==0:
            _co=3
        return _co
    
    def CornerOCW(self, _co):
        _co+=1
        if _co==4:
            _co=1
        return _co
    
    def edgeCheck (self, _side,_ori,_piece):
        if _side == "R" or _side == "L":
            for i in self.nRL:
                if i == _piece:
                    return self.oriSwap(_ori)
        elif _side == "U" or _side == "D":
            for i in self.nUD:
                if i == _piece:
                    return self.oriSwap(_ori)
        elif _side == "F" or _side == "B":
            for i in self.nFB:
                if i == _piece:
                    return self.oriSwap(_ori)
        return _ori
    
    def oriSwap (self, _ori):
        if _ori == 1:
            return 2
        elif _ori == 2:
            
# 420 lines lmfao blaze it
            
            return 1
        else: 
            print("something happened when switching orientation")
            return 
