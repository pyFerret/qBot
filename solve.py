import cube
import conversion.binaryTranslation.bincubeconvert as bcc
import json


# This is where I have put all the
# different parts of solving the cube.
# This class can create its own cube, 
# scramble it, and solve it entirely.


# TODO: add task list to this file and also the rest of them


class Solve:

    # to create a solve, give a cube to solve,
    # run "cross(), f2lfull(), oll(), and pll()"
    # and to get the moves, call "getMoves"

    def __init__(self, _cube):
        self.moves = ""
        self.fullmoves = ""
        with open("moves/movesets.json", "r") as file:
            self.movesets = json.load(file)
        self.Cube = _cube
        self.cCube = cube.Cube(True, "scrambles/solved.cube")

    def add_moves(self):
        return self.fullmoves + " " + self.moves

    def cross(self):  # solve all cross
        cross_pieces = ["b", "d", "f", "h"]
        for i, a in enumerate(cross_pieces):
            self.moves = self.crossMovements(self.locate(a), i)
            self.fullmoves = self.add_moves()
            self.execute()

    def f2l(self, pair):  # solve single f2l pair (self, pair to solve for)
        if pair == 0:
            edge = self.locate("j")
            corn = self.locate("a")
            self.moves = self.movesets["f2l"]["ja"][str(bcc.bing(edge))][str(bcc.bing(corn))]
            self.fullmoves = self.add_moves()
            self.execute()
        elif pair == 1:
            edge = self.locate("l")
            corn = self.locate("c")
            self.moves = self.movesets["f2l"]["lc"][str(bcc.bing(edge))][str(bcc.bing(corn))]
            self.fullmoves = self.add_moves()
            self.execute()
        elif pair == 2:
            edge = self.locate("o")
            corn = self.locate("g")
            self.moves = self.movesets["f2l"]["og"][str(bcc.bing(edge))][str(bcc.bing(corn))]
            self.fullmoves = self.add_moves()
            self.execute()
        elif pair == 3:
            edge = self.locate("q")
            corn = self.locate("i")
            self.moves = self.movesets["f2l"]["qi"][str(bcc.bing(edge))][str(bcc.bing(corn))]
            self.fullmoves = self.add_moves()
            self.execute()

    def fullf2l(self):  # solve all pairs
        for i in range(4):
            self.f2l(i)

    def locate(self, piece):  # locate a piece on the cube (self, piece to locate)
        return self.Cube.cube[piece]

    def crossMovements(self, cPos, step):  # find movements for cross (self, current position, cross edge)
        if step == 0:
            return self.movesets["cross"]["b"][str(cPos[1])][str(cPos[0])]
        elif step == 1:
            return self.movesets["cross"]["d"][str(cPos[1])][str(cPos[0])]
        elif step == 2:
            return self.movesets["cross"]["f"][str(cPos[1])][str(cPos[0])]
        elif step == 3:
            return self.movesets["cross"]["h"][str(cPos[1])][str(cPos[0])]

    def execute(self):  # execute current moves in virtual cube
        for i in self.moves.split():
            if i == "R":
                self.Cube.R()
            elif i == "R'":
                self.Cube.R(True)
            elif i == "R2":
                self.Cube.R()
                self.Cube.R()
            elif i == "L":
                self.Cube.L()
            elif i == "L'":
                self.Cube.L(True)
            elif i == "L2":
                self.Cube.L()
                self.Cube.L()
            elif i == "U":
                self.Cube.U()
            elif i == "U'":
                self.Cube.U(True)
            elif i == "U2":
                self.Cube.U()
                self.Cube.U()
            elif i == "D":
                self.Cube.D()
            elif i == "D'":
                self.Cube.D(True)
            elif i == "D2":
                self.Cube.D()
                self.Cube.D()
            elif i == "F":
                self.Cube.F()
            elif i == "F'":
                self.Cube.F(True)
            elif i == "F2":
                self.Cube.F()
                self.Cube.F()
            elif i == "B":
                self.Cube.B()
            elif i == "B'":
                self.Cube.B(True)
            elif i == "B2":
                self.Cube.B()
                self.Cube.B()
            else:
                print("not a valid move")

    def checkSolved(self):  # checks if the cube is solved
        wrongbool = True
        wrong = []
        for i in self.Cube.cube:
            if self.Cube.cube[i] == self.cCube.cube[i]:
                pass
            else:
                wrong.append(i)
                wrongbool = False
        return wrongbool, wrong

    def manual(self, _moves):  # I put this in to help with putting in movesets (self, moves to execute)
        self.moves = _moves
        self.execute()
        print(self.Cube.cube)
