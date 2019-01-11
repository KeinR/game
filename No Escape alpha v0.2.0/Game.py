import platform
import os
from tkinter import *
if platform.python_version()[0] == "3":
    print("You are using python 3")
elif platform.python_version()[0] == "2":
    print("ERROR: You are using Python 2. Please run with the latest version of Python 3.")
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain
try:
    import pygame
except ImportError:
    print("Module Pygame not installed. Installing now...")
    pipmain(['install', 'Pygame'])
    import pygame
from game import Script1, save_load

class game(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("555x400")
        Frame.__init__(self, self.root)
        self.create_widgets()
        pygame.init()
        self.phase = 1
        self.p = "s"
        self.sc = False
        self.sab = False

    def create_widgets(self):
        self.grid()
        self.text = Text(self, height=15, width=69, fg="black", bg="dark khaki", wrap=WORD)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.grid(column=0, row=0)

        self.root.bind('<Return>', self.input)

        self.submit = Entry(self, width=35, bg="grey")
        self.submit.grid(column=0, row=1)

    def input(self, event):
        pygame.mixer.music.stop()
        self.inp = self.submit.get()
        self.submit.delete(0, END)

        if self.inp is None:
            return None

        if self.inp == "save":
            if self.p == "s":
                self.insert("\nERROR: You cannot load at the start! Just type \"start\" instead!\n(Also it means that I don't have to spend a bunch of time making a special procedure for saving at start when there really is no need to)")
            else:
                save_load.save(self.p, self.sc, self.sab)
                self.insert("\n==SAVED==")
            return None
        if self.inp == "load":
            loadL = save_load.load()
            self.p = loadL[0][:-1]
            self.inp = loadL[0][-1]
            self.sc = loadL[1]
            self.sab = loadL[2]
            self.insert("\n==SAVE LOADED==")
        print(self.p)
        print(self.inp)
        script = None
        val = None
        if self.phase == 1:
            scriptR = Script1.Script().script(self.inp, self.p, self.sc, self.sab)
            if scriptR == None:
                return None
            val = scriptR[0]
            script = scriptR[1]
            print(scriptR)
        if self.phase == 2:
            pass
        if script == "Next":
            self.phase += 1

        if val[0] == "<":
            if val[1:-1] == "sc":
                self.sc = True
            elif val[1:-1] == "sab":
                self.sab = True
        else:
            self.p = val[:]

        self.insert(script)


    def insert(self, text):
        self.text.insert(END, text)
        self.text.see("end")
    def start(self):
        self.insert("Game by Orion O. Musselman\nWelcome to No Escape alpha v0.2.0!\nTake note that this game is still in it's developement stage and will be until v1.0.0\nBe sure to read the \"READ ME \" for instructions\nEnter \"start\" to begin . . .")
        self.root.mainloop()
    def __str__(self):
        return str(self)


if __name__ == "__main__":
    game().start()