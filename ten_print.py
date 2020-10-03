#!/usr/bin/env python3

import os
import sys

import tkinter
from random import randint
from PIL import Image

class TenPrint():
    def __init__(self, len_x, len_y, canvas, canvas_w, canvas_h):
        self.len_x = len_x
        self.len_y = len_y
        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        self.BACK_SLASH = (0, 0, self.len_x, self.len_y)
        self.FORWARD_SLASH = (0, self.len_y, self.len_x, 0)
        self.canvas = canvas


    def draw(self, save=False):
        self.canvas.delete(tkinter.ALL)

        for x in range(0, self.canvas_w, self.len_x):
            for y in range(0,self.canvas_h, self.len_y):
                case = {0: self.BACK_SLASH, 1: self.FORWARD_SLASH}
                slash = case[randint(0,1)]
                slash = (slash[0] + x, slash[1] + y,
                         slash[2] + x, slash[3] + y)

                self.canvas.create_line(*slash, fill='white')
                self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        if save:
            self.save()

    def save(self):
        self.canvas.postscript(file='tenprinted.eps')
        img = Image.open('tenprinted.eps')
        img.save('tenprinted.png', 'png')
        os.remove('tenprinted.eps')

def main():
    root = tkinter.Tk()
    root.geometry('+0+0')

    canvas_w = 400
    canvas_h = 400

    canvas = tkinter.Canvas(root, bg='black', width=canvas_w, height=canvas_h)

    tp = TenPrint(30, 30, canvas, canvas_w, canvas_h)

    if '-s' in sys.argv:
        tp.draw(save=True)
    else:
        tp.draw()

    tkinter.mainloop()

if __name__ == '__main__':
    main()
