# qBot

## DESCRIPTION

This is the source code for my current biggest project that I'm working on. The primary idea is that I am forcing a robot to solve a rubik's cube (ethically *wink wink*). I started it early in the summer of 2021 when I didn't even have access to a computer or the internet and over the past year I have made enough progress on it that the sunk cost fallacy has kicked in. there are quite a few things that I still need to do (check to-do list below), but if you have any suggestions or ideas or fixes or anything else please let me know, because this is the first robot that I've ever made solo and I am probably not very prepared for this.

---

## HOW TO USE
If you wish to run this, just run `__main__.py`. Running it will start a window where you can manipulate the cube in a couple different ways. You should originally be greeted with this screen.

![tkinter Solve tab](/assets/reference/solvescreen.png)

Here you will see a variety of buttons and boxes, and I will now go through all functionality on this tab. (:

###  __Solve Tab__

`input`; this is the text box under the `put input to any command here` text. altering the text will affect what all of the buttons do.

`list`; this button will list parts of the program in the large text box below (big white box)
 - input options; `cross` will list the cross piece positions; `moves` will list the current list of moves as they are in code; no command will list the whole cube and a boolean telling whether the cube is solved or not

`clear`; this button will clear what is currently in `input`

`full solve`; this button will create (and execute to the virtual cube) the moves to fully solve the cube (currently only solves through f2l in some cases as i have not put in all f2l cases and i have not figured out how to detect oll and pll yet)

`scramble`; this button will scramble the virtual cube based on the `input` text box.
- input options; `preset [PRESET_NAME]` will scramble the cube to a preset scramble in the scrambles folder; `[MOVES]` will scramble the cube using the moves in `input` (format is uppercase letter, apostrophe for inverted or 2 for double turn, and spaces between each turn. EX: `R' D2 R`); no command will do nothing

`cross`; this button will solve the cross of whatever scramble is given, as long as the scramble is valid (all four of the cross pieces exist)

`f2l`; this button will solve f2l(first 2 layers) pairs whether the cross has been solved or not
- input options; `pair [PAIR_NUMBER]` will solve a specific pair number (1-4); no command will solve all 4

`oll`; this button will (eventually) solve oll (orientation of the last layer)

`pll`; this button will (eventually) solve pll (permutation of the last layer)

`last layer`; this button will (eventually) solve the whole last layer (oll and pll)

`fix moves`; this button will fix the current list of moves(observable with list [moves]) to avoid redundancy in moves that cancel out or add to one another (EX: `R R2 -> R'`)

---

# DISCLAIMER
This project is still very much a work in progress. 
This will not be done for at least another few months if not a year or two.
Try not to expect too much, but if you do see an issue that might arise
please let me know.