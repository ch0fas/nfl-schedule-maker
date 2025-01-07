import pandas as pd
import numpy as np
from random import choice
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

#Window Object

class Application(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("NFL Schedule Maker")
        self.minsize(800,450)

        #Frames for each type of window

        #Title Window
        self.frame1 = Frame1(self)

        #Schedule Options Window
        self.frame2 = Frame2(self)

        #Main Window
        self.show_frame(self.frame1)
    
    def show_frame(self, frame):
        for i in self.winfo_children():
            i.pack_forget()
        frame.pack(fill="both", expand = True)



#The Main Title Window
class Frame1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(master=self, text="This is a test", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = ttk.Button(master=self, text="Go To Another WIndow", command= lambda: parent.show_frame(parent.frame2))
        self.button.pack(pady=20)

#The Window For Schedule Options

class Frame2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(master=self, text="This is another test", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = ttk.Button(master=self, text="Go Back To Start Menu", command= lambda: parent.show_frame(parent.frame1))
        self.button.pack(pady=20)

#Run Loop

if __name__ == "__main__":
    program = Application()
    program.mainloop()