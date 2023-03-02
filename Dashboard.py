import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
import Signup
import Login

class Dashboard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        main_frame = tk.Frame(self, bg="#8D99AE", height=600, width=800)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        
        self.geometry("800x600")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}
        
        lb1= Label(main_frame, text="Enter Name", width=800, font=("Verdana",20), background="dark blue")  
        lb1.place(x=0, y=0)
        
        lb2 = Label(main_frame, text="username", width=15, font=("Verdana",12), background="blue")
        lb2.place(x=30, y=60)
        
        lb3 = Label(main_frame, text="Left Hand", width=10, font=("Verdana",10))
        lb3.place(x=30,y=140)
        
        Button(main_frame, text="index", width=15, command=lambda: getlogin()).place(x=150,y=200) 
        
        
# top = Dashboard()
# top.title("Dashboard")
# top.mainloop()

# top.destroy()