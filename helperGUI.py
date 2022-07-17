# This is a tkinter window that I created in
# order to help put in commands on the fly 
# and put in algorithms without having to 
# factor the code on my own. it's pretty much
# just for ease of life, but it is still pretty
# important to the project.

from tkinter import *
from tkinter import ttk
# from PIL import ImageTk, Image
# import json
from solve import *
# from colorcubeconvert import *
from conversion.binaryTranslation.bincubeconvert import *

root = Tk()
root.title("qBot Helper GUI")

tab_parent = ttk.Notebook(root)

tab_solve = ttk.Frame(tab_parent)
tab_debug = ttk.Frame(tab_parent)
tab_cubro = ttk.Frame(tab_parent)
tab_cubev = ttk.Frame(tab_parent)

tab_parent.add(tab_solve, text="Solve")
tab_parent.add(tab_debug, text="Debug")
tab_parent.add(tab_cubro, text="Rotate")
tab_parent.add(tab_cubev, text="Cube Vis")


# DEBUG TAB


with open("moves/movesets.json", "r") as file:
    moves = json.load(file)

currentPair = ["ja", [1, 10], [0, 1]]


def next_pair():
    global currentPair
    currentPair[2][0] += 1
    if currentPair[2][0] == 4:
        currentPair[2][0] = 1
        if currentPair[2][1] == 1 or currentPair[2][1] == 7 or currentPair[2][1] == 18 or currentPair[2][1] == 24:
            currentPair[2][1] += 2
        elif currentPair[2][1] == 3 or currentPair[2][1] == 20:
            currentPair[2][1] += 4
        elif currentPair[2][1] == 9:
            currentPair[2][1] += 9
        elif currentPair[2][1] == 26:
            currentPair[2][1] = 1
            currentPair[1][0] += 1
            if currentPair[1][0] == 3:
                currentPair[1][0] = 1
                currentPair[1][1] += 2
                if currentPair[1][1] == 14:
                    currentPair[1][1] += 1
                elif currentPair[1][1] == 27:
                    if currentPair[0] == "ja":
                        currentPair = [
                            "lc",
                            [1, 12],
                            [1, 3]
                        ]
                    elif currentPair[0] == "lc":
                        currentPair = [
                            "og",
                            [1, 15],
                            [1, 7]
                        ]
                    elif currentPair[0] == "og":
                        currentPair = [
                            "qi",
                            [1, 17],
                            [1, 9]
                        ]


def check():
    try:
        lbl_done["text"] = moves["f2l"][currentPair[0]][bing(currentPair[1])][bing(currentPair[2])]
    except KeyError:
        lbl_done["text"] = "not input yet"


def load():
    global moves
    try:
        moves["f2l"][currentPair[0]][bing(currentPair[1])][bing(currentPair[2])] = txt_move.get()
    except KeyError:
        moves["f2l"][currentPair[0]].update({bing(currentPair[1]): {bing(currentPair[2]): txt_move.get()}})
    next_pair()
    lbl_pair["text"] = str(currentPair)
    check()


def skip():
    next_pair()
    lbl_pair.config(text=str(currentPair))
    check()


def save():
    with open("moves/movesets.json", "w") as new_file:
        json.dump(moves, new_file, indent=4)


def manu():
    global currentPair
    got_pair = txt_manu.get().split()
    currentPair = [got_pair[0],
                   [int(got_pair[1]), int(got_pair[2])],
                   [int(got_pair[3]), int(got_pair[4])]]
    lbl_pair["text"] = str(currentPair)
    check()


def ja():
    txt_manu.delete(0, END)
    txt_manu.insert(0, "ja ")


def lc():
    txt_manu.delete(0, END)
    txt_manu.insert(0, "lc ")


def og():
    txt_manu.delete(0, END)
    txt_manu.insert(0, "og ")


def qi():
    txt_manu.delete(0, END)
    txt_manu.insert(0, "qi ")


frm_most = Frame(tab_debug)
frm_npad = Frame(tab_debug)
frm_butt = Frame(tab_debug)
frm_jloq = Frame(frm_most)
txt_move = Entry(frm_most)
txt_manu = Entry(frm_most)
lbl_done = Label(frm_most,   text="done")
lbl_manu = Label(frm_most,   text="manual pair",                                                        width=12)
lbl_pair = Label(frm_most,   text="f2l pair",                                                           width=12)
btn_load = Button(frm_most,  text="load pair",  command=load)
btn_skip = Button(frm_most,  text="skip pair",  command=skip)
btn_save = Button(frm_most,  text="save moves", command=save)
btn_manu = Button(frm_most,  text="input pair", command=manu)
btn_ja = Button(frm_jloq,    text="ja",         command=ja,                                             width=3)
btn_lc = Button(frm_jloq,    text="lc",         command=lc,                                             width=3)
btn_og = Button(frm_jloq,    text="og",         command=og,                                             width=3)
btn_qi = Button(frm_jloq,    text="qi",         command=qi,                                             width=3)
btn_1 = Button(frm_npad,     text="1",          command=lambda: txt_manu.insert(END, "1"),              width=3)
btn_2 = Button(frm_npad,     text="2",          command=lambda: txt_manu.insert(END, "2"),              width=3)
btn_3 = Button(frm_npad,     text="3",          command=lambda: txt_manu.insert(END, "3"),              width=3)
btn_4 = Button(frm_npad,     text="4",          command=lambda: txt_manu.insert(END, "4"),              width=3)
btn_5 = Button(frm_npad,     text="5",          command=lambda: txt_manu.insert(END, "5"),              width=3)
btn_6 = Button(frm_npad,     text="6",          command=lambda: txt_manu.insert(END, "6"),              width=3)
btn_7 = Button(frm_npad,     text="7",          command=lambda: txt_manu.insert(END, "7"),              width=3)
btn_8 = Button(frm_npad,     text="8",          command=lambda: txt_manu.insert(END, "8"),              width=3)
btn_9 = Button(frm_npad,     text="9",          command=lambda: txt_manu.insert(END, "9"),              width=3)
btn_0 = Button(frm_npad,     text="0",          command=lambda: txt_manu.insert(END, "0"),              width=3)
btn_spc = Button(frm_npad,   text="spc",        command=lambda: txt_manu.insert(END, " "),              width=3)
btn_deln = Button(frm_npad,  text="del",        command=lambda: txt_manu.delete(len(txt_manu.get())-1), width=3)
btn_delm = Button(frm_butt,  text="del",        command=lambda: txt_move.delete(len(txt_move.get())-1), width=3)
btn_rn = Button(frm_butt,    text="R",          command=lambda: txt_move.insert(END, "R "),             width=3)
btn_ln = Button(frm_butt,    text="L",          command=lambda: txt_move.insert(END, "L "),             width=3)
btn_un = Button(frm_butt,    text="U",          command=lambda: txt_move.insert(END, "U "),             width=3)
btn_dn = Button(frm_butt,    text="D",          command=lambda: txt_move.insert(END, "D "),             width=3)
btn_fn = Button(frm_butt,    text="F",          command=lambda: txt_move.insert(END, "F "),             width=3)
btn_bn = Button(frm_butt,    text="B",          command=lambda: txt_move.insert(END, "B "),             width=3)
btn_ri = Button(frm_butt,    text="R'",         command=lambda: txt_move.insert(END, "R' "),            width=3)
btn_li = Button(frm_butt,    text="L'",         command=lambda: txt_move.insert(END, "L' "),            width=3)
btn_ui = Button(frm_butt,    text="U'",         command=lambda: txt_move.insert(END, "U' "),            width=3)
btn_di = Button(frm_butt,    text="D'",         command=lambda: txt_move.insert(END, "D' "),            width=3)
btn_fi = Button(frm_butt,    text="F'",         command=lambda: txt_move.insert(END, "F' "),            width=3)
btn_bi = Button(frm_butt,    text="B'",         command=lambda: txt_move.insert(END, "B' "),            width=3)
btn_r2 = Button(frm_butt,    text="R2",         command=lambda: txt_move.insert(END, "R2 "),            width=3)
btn_l2 = Button(frm_butt,    text="L2",         command=lambda: txt_move.insert(END, "L2 "),            width=3)
btn_u2 = Button(frm_butt,    text="U2",         command=lambda: txt_move.insert(END, "U2 "),            width=3)
btn_d2 = Button(frm_butt,    text="D2",         command=lambda: txt_move.insert(END, "D2 "),            width=3)
btn_f2 = Button(frm_butt,    text="F2",         command=lambda: txt_move.insert(END, "F2 "),            width=3)
btn_b2 = Button(frm_butt,    text="B2",         command=lambda: txt_move.insert(END, "B2 "),            width=3)
btn_clr = Button(frm_butt,   text="clr",        command=lambda: txt_move.delete(0, END),                width=3)

frm_most.grid(row=0, column=0)
frm_npad.grid(row=0, column=1)
frm_butt.grid(row=0, column=2)

lbl_pair.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
btn_load.grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
btn_skip.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
txt_move.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
btn_save.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")
lbl_done.grid(row=5, column=0, padx=1, pady=1, sticky="nesw")

frm_jloq.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")
lbl_manu.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
txt_manu.grid(row=1, column=1, padx=1, pady=1, sticky="nesw")
btn_manu.grid(row=2, column=1, padx=1, pady=1, sticky="nesw")
btn_ja.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
btn_lc.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
btn_og.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")
btn_qi.grid(row=0, column=3, padx=1, pady=1, sticky="nesw")

btn_1.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
btn_2.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
btn_3.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")
btn_4.grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
btn_5.grid(row=1, column=1, padx=1, pady=1, sticky="nesw")
btn_6.grid(row=1, column=2, padx=1, pady=1, sticky="nesw")
btn_7.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
btn_8.grid(row=2, column=1, padx=1, pady=1, sticky="nesw")
btn_9.grid(row=2, column=2, padx=1, pady=1, sticky="nesw")
btn_spc.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
btn_0.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")
btn_deln.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")

btn_rn.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
btn_ln.grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
btn_un.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
btn_dn.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
btn_fn.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")
btn_bn.grid(row=5, column=0, padx=1, pady=1, sticky="nesw")
btn_ri.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
btn_li.grid(row=1, column=1, padx=1, pady=1, sticky="nesw")
btn_ui.grid(row=2, column=1, padx=1, pady=1, sticky="nesw")
btn_di.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")
btn_fi.grid(row=4, column=1, padx=1, pady=1, sticky="nesw")
btn_bi.grid(row=5, column=1, padx=1, pady=1, sticky="nesw")
btn_r2.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")
btn_l2.grid(row=1, column=2, padx=1, pady=1, sticky="nesw")
btn_u2.grid(row=2, column=2, padx=1, pady=1, sticky="nesw")
btn_d2.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")
btn_f2.grid(row=4, column=2, padx=1, pady=1, sticky="nesw")
btn_b2.grid(row=5, column=2, padx=1, pady=1, sticky="nesw")
btn_delm.grid(row=0, column=3, padx=1, pady=1, sticky="nesw")
btn_clr.grid(row=1, column=3, padx=1, pady=1, sticky="nesw")


# SOLVE TAB


solve = Solve(cube.Cube(True, "scrambles/solved.cube"))


def scmbl():
    scramble = txt_enter.get().split()
    if scramble[0] == "preset":
        scramble[1] = "scrambles/" + scramble[1] + ".cube"
        solve.Cube = cube.Cube(True, scramble[1])
    else:
        solve.moves = txt_enter.get()
        solve.execute()


def ftwol():
    command = txt_enter.get().split()
    if len(command) == 0:
        solve.fullf2l()
    elif command[0] == "pair":
        solve.f2l(int(command[1]) - 1)


def oll():
    pass


def pll():
    pass


def lastl():
    oll()
    pll()


def box_nl():
    box_list.insert(END, "\n")


def box():
    if txt_enter.get() == "cross":
        box_list.insert(END, str(solve.Cube.cube["b"]))
        box_list.insert(END, str(solve.Cube.cube["d"]))
        box_list.insert(END, str(solve.Cube.cube["f"]))
        box_list.insert(END, str(solve.Cube.cube["h"]))
        box_nl()
    elif txt_enter.get() == "moves":
        box_list.insert(END, solve.fullmoves)
        box_nl()
    elif txt_enter.get().split()[0] == "binary":
        form_bin(txt_enter.get().split()[1], solve.Cube.cube)
    else: 
        for i in solve.Cube.cube:
            box_list.insert(END, str(solve.Cube.cube[i]))
            box_nl()
        box_list.insert(END, solve.checkSolved())
        box_nl()


def fix():
    with open("moves/movevalues.json") as new_file:
        movefix = json.load(new_file)
    moves_list = solve.fullmoves.split()
    final_list = ""
    fixed = False
    for i in range(len(moves_list)):
        try:
            if not fixed:
                if moves_list[i][0] == "R" and moves_list[i + 1][0] == "R":
                    fix_sum = movefix["R"][moves_list[i]] + movefix["R"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "R "
                    elif fix_sum == 2:
                        final_list += "R2 "
                    elif fix_sum == 3:
                        final_list += "R' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "R2"
                    fixed = True
                elif moves_list[i][0] == "L" and moves_list[i + 1][0] == "L":
                    fix_sum = movefix["L"][moves_list[i]] + movefix["L"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "L "
                    elif fix_sum == 2:
                        final_list += "L2 "
                    elif fix_sum == 3:
                        final_list += "L' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "L2"
                    fixed = True
                elif moves_list[i][0] == "U" and moves_list[i + 1][0] == "U":
                    fix_sum = movefix["U"][moves_list[i]] + movefix["U"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "U "
                    elif fix_sum == 2:
                        final_list += "U2 "
                    elif fix_sum == 3:
                        final_list += "U' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "U2"
                    fixed = True
                elif moves_list[i][0] == "D" and moves_list[i + 1][0] == "D":
                    fix_sum = movefix["D"][moves_list[i]] + movefix["D"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "D "
                    elif fix_sum == 2:
                        final_list += "D2 "
                    elif fix_sum == 3:
                        final_list += "D' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "D2"
                    fixed = True
                elif moves_list[i][0] == "F" and moves_list[i + 1][0] == "F":
                    fix_sum = movefix["F"][moves_list[i]] + movefix["F"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "F "
                    elif fix_sum == 2:
                        final_list += "F2 "
                    elif fix_sum == 3:
                        final_list += "F' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "F2"
                    fixed = True
                elif moves_list[i][0] == "B" and moves_list[i + 1][0] == "B":
                    fix_sum = movefix["B"][moves_list[i]] + movefix["B"][moves_list[i + 1]]
                    if fix_sum == 0:
                        final_list += ""
                    elif fix_sum == 1:
                        final_list += "B "
                    elif fix_sum == 2:
                        final_list += "B2 "
                    elif fix_sum == 3:
                        final_list += "B' "
                    elif fix_sum == 4:
                        final_list += ""
                    elif fix_sum == -2:
                        final_list += "B2"
                    fixed = True
                else:
                    final_list += moves_list[i] + " "
            else:
                fixed = False
        except IndexError:
            final_list += moves_list[i]
    solve.fullmoves = final_list


def clear():
    txt_enter.delete(0, END)


def fullSolve():

    # 420 lines lmfao blaze it

    solve.cross()
    solve.fullf2l()


frm_grid = Frame(tab_solve)
frm_last = Frame(frm_grid)
box_list = Text(tab_solve)
txt_enter = Entry(frm_grid,                                          width=30)
lbl_enter = Label(frm_grid,  text="put input to any command here")
btn_scmbl = Button(frm_grid, text="scramble",   command=scmbl,       width=30)
btn_cross = Button(frm_grid, text="cross",      command=solve.cross)
btn_ftwol = Button(frm_grid, text="f2l",        command=ftwol)
btn_print = Button(frm_grid, text="list",       command=box)
btn_clear = Button(frm_grid, text="clear",      command=clear)
btn_full = Button(frm_grid,  text="full solve", command=fullSolve)
btn_oll = Button(frm_last,   text="oll",        command=oll,         width=10)
btn_pll = Button(frm_last,   text="pll",        command=pll,         width=10)
btn_lastl = Button(frm_last, text="last layer", command=lastl,       width=10)
btn_fix = Button(frm_grid,   text="fix moves",  command=fix)

lbl_enter.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
txt_enter.grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
btn_scmbl.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
btn_cross.grid(row=1, column=1, padx=1, pady=1, sticky="nesw")
btn_ftwol.grid(row=2, column=1, padx=1, pady=1, sticky="nesw")
btn_print.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
btn_clear.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
btn_full.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")
frm_last.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")
btn_oll.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")
btn_pll.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")
btn_lastl.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")
btn_fix.grid(row=4, column=1, padx=1, pady=1, sticky="nesw")

frm_grid.pack()
box_list.pack()


# ROTATE TAB


def rotate(rotate_dir):
    rotate_input = txt_rotateInput.get()
    rotate_output = ""
    rotations = json.load(open("moves/rotations.json"))
    for i in rotate_input.split(" "):
        rotate_output += rotations[rotate_dir][i] + " "
    txt_rotateOutput.delete(0, END)
    txt_rotateOutput.insert(END, rotate_output[:-1])


frm_rotateCube = Frame(tab_cubro)
frm_rotateIO = Frame(tab_cubro)

frm_rotateButtons = Frame(frm_rotateCube)

btn_xn = Button(frm_rotateButtons, text="X",  command=lambda: rotate("X"),  width=3)
btn_xi = Button(frm_rotateButtons, text="X'", command=lambda: rotate("X'"), width=3)
btn_yn = Button(frm_rotateButtons, text="Y",  command=lambda: rotate("Y"),  width=3)
btn_yi = Button(frm_rotateButtons, text="Y'", command=lambda: rotate("Y'"), width=3)
btn_zn = Button(frm_rotateButtons, text="Z",  command=lambda: rotate("Z"),  width=3)
btn_zi = Button(frm_rotateButtons, text="Z'", command=lambda: rotate("Z'"), width=3)

btn_xn.grid(column=0, row=0, padx=1, pady=1, sticky="nesw")
btn_xi.grid(column=1, row=0, padx=1, pady=1, sticky="nesw")
btn_yn.grid(column=0, row=1, padx=1, pady=1, sticky="nesw")
btn_yi.grid(column=1, row=1, padx=1, pady=1, sticky="nesw")
btn_zn.grid(column=0, row=2, padx=1, pady=1, sticky="nesw")
btn_zi.grid(column=1, row=2, padx=1, pady=1, sticky="nesw")

frm_rotateButtons.pack()

btn_rotateDelete = Button(frm_rotateCube, text="Delete", width=15)  # TODO: make the delete button do something

btn_rotateDelete.pack()

frm_rotateCube.pack()

lbl_rotateInput = Label(frm_rotateIO, text="input moves to rotate here")
txt_rotateInput = Entry(frm_rotateIO, width=25)
lbl_rotateOutput = Label(frm_rotateIO, text="rotated moves will appear here")
txt_rotateOutput = Entry(frm_rotateIO, width=25)

lbl_rotateInput.grid(column=0, row=0, padx=1, pady=2, sticky="nesw")
txt_rotateInput.grid(column=0, row=1, padx=1, pady=2, sticky="nesw")
lbl_rotateOutput.grid(column=0, row=2, padx=1, pady=2, sticky="nesw")
txt_rotateOutput.grid(column=0, row=3, padx=1, pady=2, sticky="nesw")

frm_rotateIO.pack(pady=5)

tab_parent.pack(expand=1, fill="both")

"""
## CUBEVIS TAB


image = colorconverter(solve.Cube.cube)
img = ImageTk.PhotoImage(Image.open("assets/visualizer/cubevis.png").resize((600, 450), resample=Image.NEAREST))

def updatecube():
    image.update()
    img = ImageTk.PhotoImage(Image.open("assets/visualizer/cubevis.png").resize((600, 450), resample=Image.NEAREST))
    lbl_img.configure(image=img)
    lbl_img.image = img

lbl_img = Label(tab_cubev, image = img)
btn_update = Button(tab_cubev, text="update image", command=updatecube)

lbl_img.pack()
btn_update.pack()
"""
root.mainloop()
