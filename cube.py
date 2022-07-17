import conversion.binaryTranslation.bincubeconvert as bcc

# This file contains the class that I use to dictate what a cube is
# If you would like a new cube you can just make one with this class


class Cube:

    # the virtual cube, in most files that it is accessed, 
    # is held with the Green side facing and the White side 
    # up. comments from this point on will be based on that.

    def __init__(self, sort, scramble):
        self.cube = bcc.form_cube(sort, scramble)
        # this is the actual virtual
        # cube. the rest of the class
        # is manipulation of said actual
        # virtual cube

        self.nRL = ["b", "h", "s", "y"]  # nRL stands for Not Right or Left
        self.nUD = ["j", "l", "o", "q"]  # nUD stands for Not Up or Down
        self.nFB = ["d", "f", "u", "w"]  # nFB stands for Not Front or Back
        # these three lists are used as lists of the edges not found on two
        # opposite sides (like not right or left side edges)

    def piece_change(self, p, x):  # this will basically change where a piece is.
        self.cube[p][1] = x        # it's probably not the best way to do it, but I don't really care

    def ori_corner(self, p, w):  # this will change the orientation of a corner
        self.cube[p][0] = self.corner_OCW(self.cube[p][0]) if w == "OCW" else self.corner_OCCW(self.cube[p][0])

    def ori_edge(self, p, s):  # this will change the orientation of an edge
        self.cube[p][0] = self.edge_check(s, self.cube[p][0], p)

    def R(self, _inverted=False):  # this function will turn the right (red) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (R -> R')
            for i in self.cube:
                i = str(i)
                # I'm looking at this now, and I feel like these two lines
                # could be a lot better if I didn't do the second one,
                # and instead made it a separate variable. I think I
                # will change it in the future, but I don't have time rn

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]  # the location of the piece being dealt with currently

                if piece == 9:  # the next_pair four ifs move the corners around the right side
                    self.piece_change(i, 26)
                    self.ori_corner(i, "OCW")
                elif piece == 3:
                    self.piece_change(i, 9)
                    self.ori_corner(i, "OCCW")
                elif piece == 20:
                    self.piece_change(i, 3)
                    self.ori_corner(i, "OCW")
                elif piece == 26:
                    self.piece_change(i, 20)
                    self.ori_corner(i, "OCCW")
                elif piece == 6:  # the next_pair four ifs move the edges around the right side
                    self.piece_change(i, 17)
                    self.ori_edge(i, "R")
                elif piece == 12:
                    self.piece_change(i, 6)
                    self.ori_edge(i, "R")
                elif piece == 23:
                    self.piece_change(i, 12)
                    self.ori_edge(i, "R")
                elif piece == 17:
                    self.piece_change(i, 23)
                    self.ori_edge(i, "R")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 9:  # the next_pair four ifs move the corners around the right side
                    self.piece_change(i, 3)
                    self.ori_corner(i, "OCW")
                elif piece == 3:
                    self.piece_change(i, 20)
                    self.ori_corner(i, "OCCW")
                elif piece == 20:
                    self.piece_change(i, 26)
                    self.ori_corner(i, "OCW")
                elif piece == 26:
                    self.piece_change(i, 9)
                    self.ori_corner(i, "OCCW")
                elif piece == 6:  # the next_pair four ifs move the edges around the right side
                    self.piece_change(i, 12)
                    self.ori_edge(i, "R")
                elif piece == 12:
                    self.piece_change(i, 23)
                    self.ori_edge(i, "R")
                elif piece == 23:
                    self.piece_change(i, 17)
                    self.ori_edge(i, "R")
                elif piece == 17:
                    self.piece_change(i, 6)
                    self.ori_edge(i, "R")

    def L(self, _inverted=False):  # this function will turn the left (orange) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (L -> L')
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 1:
                    self.piece_change(i, 18)
                    self.ori_corner(i, "OCW")
                elif piece == 18:
                    self.piece_change(i, 24)
                    self.ori_corner(i, "OCCW")
                elif piece == 24:
                    self.piece_change(i, 7)
                    self.ori_corner(i, "OCW")
                elif piece == 7:
                    self.piece_change(i, 1)
                    self.ori_corner(i, "OCCW")
                elif piece == 4:
                    self.piece_change(i, 10)
                    self.ori_edge(i, "L")
                elif piece == 10:
                    self.piece_change(i, 21)
                    self.ori_edge(i, "L")
                elif piece == 21:
                    self.piece_change(i, 15)
                    self.ori_edge(i, "L")
                elif piece == 15:
                    self.piece_change(i, 4)
                    self.ori_edge(i, "L")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 1:
                    self.piece_change(i, 7)
                    self.ori_corner(i, "OCW")
                elif piece == 7:
                    self.piece_change(i, 24)
                    self.ori_corner(i, "OCCW")
                elif piece == 24:
                    self.piece_change(i, 18)
                    self.ori_corner(i, "OCW")
                elif piece == 18:
                    self.piece_change(i, 1)
                    self.ori_corner(i, "OCCW")
                elif piece == 4:
                    self.piece_change(i, 15)
                    self.ori_edge(i, "L")
                elif piece == 15:
                    self.piece_change(i, 21)
                    self.ori_edge(i, "L")
                elif piece == 21:
                    self.piece_change(i, 10)
                    self.ori_edge(i, "L")
                elif piece == 10:
                    self.piece_change(i, 4)
                    self.ori_edge(i, "L")

    def U(self, _inverted=False):  # this function will turn the up (white) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (U -> U')
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 9:
                    self.piece_change(i, 3)
                elif piece == 3:
                    self.piece_change(i, 1)
                elif piece == 1:
                    self.piece_change(i, 7)
                elif piece == 7:
                    self.piece_change(i, 9)
                elif piece == 6:
                    self.piece_change(i, 2)
                    self.ori_edge(i, "U")
                elif piece == 2:
                    self.piece_change(i, 4)
                    self.ori_edge(i, "U")
                elif piece == 4:
                    self.piece_change(i, 8)
                    self.ori_edge(i, "U")
                elif piece == 8:
                    self.piece_change(i, 6)
                    self.ori_edge(i, "U")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 9:
                    self.piece_change(i, 7)
                elif piece == 7:
                    self.piece_change(i, 1)
                elif piece == 1:
                    self.piece_change(i, 3)
                elif piece == 3:
                    self.piece_change(i, 9)
                elif piece == 6:
                    self.piece_change(i, 8)
                    self.ori_edge(i, "U")
                elif piece == 8:
                    self.piece_change(i, 4)
                    self.ori_edge(i, "U")
                elif piece == 4:
                    self.piece_change(i, 2)
                    self.ori_edge(i, "U")
                elif piece == 2:
                    self.piece_change(i, 6)
                    self.ori_edge(i, "U")

    def D(self, _inverted=False):  # this function will turn the down (yellow) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (D -> D')
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 18:
                    self.piece_change(i, 20)
                elif piece == 20:
                    self.piece_change(i, 26)
                elif piece == 26:
                    self.piece_change(i, 24)
                elif piece == 24:
                    self.piece_change(i, 18)
                elif piece == 19:
                    self.piece_change(i, 23)
                    self.ori_edge(i, "D")
                elif piece == 23:
                    self.piece_change(i, 25)
                    self.ori_edge(i, "D")
                elif piece == 25:
                    self.piece_change(i, 21)
                    self.ori_edge(i, "D")
                elif piece == 21:
                    self.piece_change(i, 19)
                    self.ori_edge(i, "D")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 18:
                    self.piece_change(i, 24)
                elif piece == 24:
                    self.piece_change(i, 26)
                elif piece == 26:
                    self.piece_change(i, 20)
                elif piece == 20:
                    self.piece_change(i, 18)
                elif piece == 19:
                    self.piece_change(i, 21)
                    self.ori_edge(i, "D")
                elif piece == 21:
                    self.piece_change(i, 25)
                    self.ori_edge(i, "D")
                elif piece == 25:
                    self.piece_change(i, 23)
                    self.ori_edge(i, "D")
                elif piece == 23:
                    self.piece_change(i, 19)
                    self.ori_edge(i, "D")

    def F(self, _inverted=False):  # this function will turn the front (green) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (F -> F')
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 9:
                    self.piece_change(i, 7)
                    self.ori_corner(i, "OCCW")
                elif piece == 7:
                    self.piece_change(i, 24)
                    self.ori_corner(i, "OCW")
                elif piece == 24:
                    self.piece_change(i, 26)
                    self.ori_corner(i, "OCCW")
                elif piece == 26:
                    self.piece_change(i, 9)
                    self.ori_corner(i, "OCW")
                elif piece == 8:
                    self.piece_change(i, 15)
                    self.ori_edge(i, "F")
                elif piece == 15:
                    self.piece_change(i, 25)
                    self.ori_edge(i, "F")
                elif piece == 25:
                    self.piece_change(i, 17)
                    self.ori_edge(i, "F")
                elif piece == 17:
                    self.piece_change(i, 8)
                    self.ori_edge(i, "F")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 9:
                    self.piece_change(i, 26)
                    self.ori_corner(i, "OCCW")
                elif piece == 26:
                    self.piece_change(i, 24)
                    self.ori_corner(i, "OCW")
                elif piece == 24:
                    self.piece_change(i, 7)
                    self.ori_corner(i, "OCCW")
                elif piece == 7:
                    self.piece_change(i, 9)
                    self.ori_corner(i, "OCW")
                elif piece == 8:
                    self.piece_change(i, 17)
                    self.ori_edge(i, "F")
                elif piece == 17:
                    self.piece_change(i, 25)
                    self.ori_edge(i, "F")
                elif piece == 25:
                    self.piece_change(i, 15)
                    self.ori_edge(i, "F")
                elif piece == 15:
                    self.piece_change(i, 8)
                    self.ori_edge(i, "F")

    def B(self, _inverted=False):  # this function will turn the back (blue) side clockwise (unless inverted is true)
        if _inverted:              # if its inverted it will do the inverse move (B -> B')
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 1:
                    self.piece_change(i, 3)
                    self.ori_corner(i, "OCCW")
                elif piece == 3:
                    self.piece_change(i, 20)
                    self.ori_corner(i, "OCW")
                elif piece == 20:
                    self.piece_change(i, 18)
                    self.ori_corner(i, "OCCW")
                elif piece == 18:
                    self.piece_change(i, 1)
                    self.ori_corner(i, "OCW")
                elif piece == 2:
                    self.piece_change(i, 12)
                    self.ori_edge(i, "B")
                elif piece == 12:
                    self.piece_change(i, 19)
                    self.ori_edge(i, "B")
                elif piece == 19:
                    self.piece_change(i, 10)
                    self.ori_edge(i, "B")
                elif piece == 10:
                    self.piece_change(i, 2)
                    self.ori_edge(i, "B")
        else:
            for i in self.cube:
                i = str(i)

                # TODO: consolidate i = str(i)

                piece = self.cube[i][1]

                if piece == 1:
                    self.piece_change(i, 18)
                    self.ori_corner(i, "OCCW")
                elif piece == 18:
                    self.piece_change(i, 20)
                    self.ori_corner(i, "OCW")
                elif piece == 20:
                    self.piece_change(i, 3)
                    self.ori_corner(i, "OCCW")
                elif piece == 3:
                    self.piece_change(i, 1)
                    self.ori_corner(i, "OCW")
                elif piece == 2:
                    self.piece_change(i, 10)
                    self.ori_edge(i, "B")
                elif piece == 10:
                    self.piece_change(i, 19)
                    self.ori_edge(i, "B")
                elif piece == 19:
                    self.piece_change(i, 12)
                    self.ori_edge(i, "B")
                elif piece == 12:
                    self.piece_change(i, 2)
                    self.ori_edge(i, "B")
    # TODO: figure out what the fuck static means

                    # 420 lines lmfao blaze it

    # that task is a joke i know what it means i just need to figure out how to fix it
    def corner_OCCW(self, _co):
        _co -= 1
        if _co == 0:
            _co = 3
        return _co

    def corner_OCW(self, _co):
        _co += 1
        if _co == 4:
            _co = 1
        return _co

    def edge_check(self, _side, _ori, _piece):
        if _side == "R" or _side == "L":
            for i in self.nRL:
                if i == _piece:
                    return self.ori_swap(_ori)
        elif _side == "U" or _side == "D":
            for i in self.nUD:
                if i == _piece:
                    return self.ori_swap(_ori)
        elif _side == "F" or _side == "B":
            for i in self.nFB:
                if i == _piece:
                    return self.ori_swap(_ori)
        return _ori

    def ori_swap(self, _ori):
        if _ori == 1:
            return 2
        elif _ori == 2:
            return 1
        else: 
            print("something happened when switching orientation")
            return 
