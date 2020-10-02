#!/usr/bin/env python3

import tkinter
from random import randint

LEN = 30
BACK_SLASH = (0, 0, LEN, LEN)
FORWARD_SLASH = (0, LEN, LEN, 0)

def ten_print():
    global canvas
    canvas.delete(tkinter.ALL)


    for x in range(0, 400, LEN):
        for y in range(0, 400, LEN):
            case = {0: BACK_SLASH, 1: FORWARD_SLASH}
            slash = case[randint(0,1)]
            slash = (slash[0] + x, slash[1] + y,
                     slash[2] + x, slash[3] + y)

            canvas.create_line(*slash, fill='white')
            canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

def main():
    global canvas
    root = tkinter.Tk()
    root.geometry('+0+0')


    canvas = tkinter.Canvas(root, bg='black', width=400, height=400)

    ten_print()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
