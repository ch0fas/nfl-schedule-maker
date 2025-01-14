import pandas as pd
import numpy as np
from random import choice
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

#Window Objects

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

        #App Credits
        self.frame3 = Frame3(self)

        #Main Window - Correction
        self.show_frame(self.frame1)
    
    def show_frame(self, frame):
        for i in self.winfo_children():
            i.pack_forget()
        frame.pack(fill="both", expand = True)



#The Main Title Window
class Frame1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #variables

        #main title window widgets
        main_title = ttk.Label(master=self, text="🌴 NFL Schedule Maker", font=("Consolas", 48), anchor="center", 
                               background="crimson", relief="raised")
        create_schedule = ttk.Button(master=self, text="Create New Schedule")
        schedule_optns = ttk.Label(master=self, text="Schedule Options", font=("JetBrains Mono", 32), anchor="center",
                                   relief="raised")
        primetime_optn = ttk.Checkbutton(master=self, text="Choose times for primetime games", onvalue=True)
        app_creds = ttk.Button(master=self, text="App Credits", command= lambda: parent.show_frame(parent.frame3))
        old_sched = ttk.Button(master=self, text="Open Old Schedule")

        #Grid Configure
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #Grid
        main_title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=1, pady=1)
        create_schedule.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        schedule_optns.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        primetime_optn.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        app_creds.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        old_sched.grid(row=1, column=2, rowspan=4, sticky="nsew", padx=1, pady=1)


#The Window For Schedule Optionss

class Frame2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(master=self, text="This is another test", font=("JetBrains Mono", 16))
        self.label.pack(pady=20)

        self.button = ttk.Button(master=self, text="Go Back To Start Menu", command= lambda: parent.show_frame(parent.frame1))
        self.button.pack(pady=20)

class Frame3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Credits - Widgets
        text = ttk.Label(master=self, text="This project is made with 💌 by Sofia")
        go_back = ttk.Button(master=self, text="Return to Main Page", command= lambda: parent.show_frame(parent.frame1))

        #Pack
        text.pack()
        go_back.pack(fill="both")

#Run Loop

if __name__ == "__main__":
    program = Application()
    program.mainloop()