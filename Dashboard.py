import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from prettytable import PrettyTable
import subprocess

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
        
        lb2 = Label(main_frame, text="username", width=15, height=2, font=("Verdana",12), background="blue")
        lb2.place(x=600, y=60)
        
        # lb3 = Label(main_frame, text="Record", width=10, font=("Verdana",10))
        # lb3.place(x=30,y=140)
        
        Button(main_frame, text="Record", width=18, command=lambda: run_script()).place(x=600,y=150) 
        
        # table = PrettyTable(['Subject Code', 'Subject', 'Marks'])
        # print(table)
        
        Button(main_frame, text="List Angles", width=18, command=lambda: list_angles()).place(x=20,y=50) 
        
    
        def run_script():
            subprocess.call(['python', 'fing_rom_live.py'])
        
        def list_angles():
            print("Angles")
            query = "Select * from patients"
            print(query)
            db_conn.mycursor.execute(query)
            row = db_conn.mycursor.fetchall()
            for ang in row:
                print(ang)
                ang = Label(main_frame,text=ang)
                ang.pack()
        
        
# top = Dashboard()
# top.title("Dashboard")
# top.mainloop()

# top.destroy()