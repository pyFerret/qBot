import binaryTranslation.bincubeconvert as bincubeconvert

class Cube():
    def __init__(self, sort, scramble):
        self.cube = bincubeconvert.formCube(sort, scramble)
        self.nRL = ["b", "h", "s", "y"]
        self.nUD = ["j", "l", "o", "q"]
        self.nFB = ["d", "f", "u", "w"]
    
    def R(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("R", self.cube[i][0], i)
        if _inverted: # if its inverted it will preself.cube the inverse move ( R -> R')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(26)
                    oriChange("OCW")
                elif piece == 3:
                    pieceChange(9)
                    oriChange("OCCW")
                elif piece == 20:
                    pieceChange(3)
                    oriChange("OCW")
                elif piece == 26:
                    pieceChange(20)
                    oriChange("OCCW")
                elif piece == 6:
                    pieceChange(17)
                    oriEdge()
                elif piece == 12:
                    pieceChange(6)
                    oriEdge()
                elif piece == 23:
                    pieceChange(12)
                    oriEdge()
                elif piece == 17:
                    pieceChange(23)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(3)
                    oriChange("OCW")
                elif piece == 3:
                    pieceChange(20)
                    oriChange("OCCW")
                elif piece == 20:
                    pieceChange(26)
                    oriChange("OCW")
                elif piece == 26:
                    pieceChange(9)
                    oriChange("OCCW")
                elif piece == 6:
                    pieceChange(12)
                    oriEdge()
                elif piece == 12:
                    pieceChange(23)
                    oriEdge()
                elif piece == 23:
                    pieceChange(17)
                    oriEdge()
                elif piece == 17:
                    pieceChange(6)
                    oriEdge()
    
    def L(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("L", self.cube[i][0], i)
        if _inverted: # if its inverted it will preself.cube the inverse move ( L -> L')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    pieceChange(18)
                    oriChange("OCW")
                elif piece == 18:
                    pieceChange(24)
                    oriChange("OCCW")
                elif piece == 24:
                    pieceChange(7)
                    oriChange("OCW")
                elif piece == 7:
                    pieceChange(1)
                    oriChange("OCCW")
                elif piece == 4:
                    pieceChange(10)
                    oriEdge()
                elif piece == 10:
                    pieceChange(21)
                    oriEdge()
                elif piece == 21:
                    pieceChange(15)
                    oriEdge()
                elif piece == 15:
                    pieceChange(4)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    pieceChange(7)
                    oriChange("OCW")
                elif piece == 7:
                    pieceChange(24)
                    oriChange("OCCW")
                elif piece == 24:
                    pieceChange(18)
                    oriChange("OCW")
                elif piece == 18:
                    pieceChange(1)
                    oriChange("OCCW")
                elif piece == 4:
                    pieceChange(15)
                    oriEdge()
                elif piece == 15:
                    pieceChange(21)
                    oriEdge()
                elif piece == 21:
                    pieceChange(10)
                    oriEdge()
                elif piece == 10:
                    pieceChange(4)
                    oriEdge()
    
    def U(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("U", self.cube[i][0], i)
        if _inverted == False: # this one has to be false because i fucked up and didn't feel like switching all of the numbers whoops
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(7)
                elif piece == 7:
                    pieceChange(1)
                elif piece == 1:
                    pieceChange(3)
                elif piece == 3:
                    pieceChange(9)
                elif piece == 6:
                    pieceChange(8)
                    oriEdge()
                elif piece == 8:
                    pieceChange(4)
                    oriEdge()
                elif piece == 4:
                    pieceChange(2)
                    oriEdge()
                elif piece == 2:
                    pieceChange(6)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(3)
                elif piece == 3:
                    pieceChange(1)
                elif piece == 1:
                    pieceChange(7)
                elif piece == 7:
                    pieceChange(9)
                elif piece == 6:
                    pieceChange(2)
                    oriEdge()
                elif piece == 2:
                    pieceChange(4)
                    oriEdge()
                elif piece == 4:
                    pieceChange(8)
                    oriEdge()
                elif piece == 8:
                    pieceChange(6)
                    oriEdge()
    
    def D(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("D", self.cube[i][0], i)
        if _inverted: # if its inverted it will preself.cube the inverse move ( D -> D')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 18:
                    pieceChange(20)
                elif piece == 20:
                    pieceChange(26)
                elif piece == 26:
                    pieceChange(24)
                elif piece == 24:
                    pieceChange(18)
                elif piece == 19:
                    pieceChange(23)
                    oriEdge()
                elif piece == 23:
                    pieceChange(25)
                    oriEdge()
                elif piece == 25:
                    pieceChange(21)
                    oriEdge()
                elif piece == 21:
                    pieceChange(19)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 18:
                    pieceChange(24)
                elif piece == 24:
                    pieceChange(26)
                elif piece == 26:
                    pieceChange(20)
                elif piece == 20:
                    pieceChange(18)
                elif piece == 19:
                    pieceChange(21)
                    oriEdge()
                elif piece == 21:
                    pieceChange(25)
                    oriEdge()
                elif piece == 25:
                    pieceChange(23)
                    oriEdge()
                elif piece == 23:
                    pieceChange(19 )
                    oriEdge()
    
    def F(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("F", self.cube[i][0], i)
        if _inverted: # if its inverted it will preself.cube the inverse move ( F -> F')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(7)
                    oriChange("OCCW")
                elif piece == 7:
                    pieceChange(24)
                    oriChange("OCW")
                elif piece == 24:
                    pieceChange(26)
                    oriChange("OCCW")
                elif piece == 26:
                    pieceChange(9)
                    oriChange("OCW")
                elif piece == 8:
                    pieceChange(15)
                    oriEdge()
                elif piece == 15:
                    pieceChange(25)
                    oriEdge()
                elif piece == 25:
                    pieceChange(17)
                    oriEdge()
                elif piece == 17:
                    pieceChange(8)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 9:
                    pieceChange(26)
                    oriChange("OCCW")
                elif piece == 26:
                    pieceChange(24)
                    oriChange("OCW")
                elif piece == 24:
                    pieceChange(7)
                    oriChange("OCCW")
                elif piece == 7:
                    pieceChange(9)
                    oriChange("OCW")
                elif piece == 8:
                    pieceChange(17)
                    oriEdge()
                elif piece == 17:
                    pieceChange(25)
                    oriEdge()
                elif piece == 25:
                    pieceChange(15)
                    oriEdge()
                elif piece == 15:
                    pieceChange(8)
                    oriEdge()
    
    def B(self, _inverted = False):
        def pieceChange(x): self.cube[i][1] = x
        def oriChange(_way): self.cube[i][0] = self.CornerOCW(self.cube[i][0]) if _way == "OCW" else self.CornerOCCW(self.cube[i][0])
        def oriEdge(): self.cube[i][0] = self.edgeCheck("B", self.cube[i][0], i)
        if _inverted: # if its inverted it will preself.cube the inverse move ( B -> B')
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    pieceChange(3)
                    oriChange("OCCW")
                elif piece == 3:
                    pieceChange(20)
                    oriChange("OCW")
                elif piece == 20:
                    pieceChange(18)
                    oriChange("OCCW")
                elif piece == 18:
                    pieceChange(1)
                    oriChange("OCW")
                elif piece == 2:
                    pieceChange(12)
                    oriEdge()
                elif piece == 12:
                    pieceChange(19)
                    oriEdge()
                elif piece == 19:
                    pieceChange(10)
                    oriEdge()
                elif piece == 10:
                    pieceChange(2)
                    oriEdge()
        else:
            for i in self.cube:
                i = str(i)
    
                piece = self.cube[i][1]
    
                if piece == 1:
                    pieceChange(18)
                    oriChange("OCCW")
                elif piece == 18:
                    pieceChange(20)
                    oriChange("OCW")
                elif piece == 20:
                    pieceChange(3)
                    oriChange("OCCW")
                elif piece == 3:
                    pieceChange(1)
                    oriChange("OCW")
                elif piece == 2:
                    pieceChange(10)
                    oriEdge()
                elif piece == 10:
                    pieceChange(19)
                    oriEdge()
                elif piece == 19:
                    pieceChange(12)
                    oriEdge()
                elif piece == 12:
                    pieceChange(2)
                    oriEdge()
    
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
            return 1
        else: 
            print("something happened when switching orientation")
            return 

# 420 lines lmfao blaze it