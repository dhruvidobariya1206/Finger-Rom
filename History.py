import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
from Signup import *
import Dashboard


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # self.user=user
        # self.phone=phone

        # this is the background
        main_frame = tk.Frame(self, bg="#1c4966", height=450, width=300)
        main_frame.pack(fill="both", expand="true")

        self.geometry("450x300")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16),
                        "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}

        
        

# top = LoginPage()
# top.title("Login Page")
# top.mainloop()

# top.destroy()
