import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

import left_right as lr
import mediapipe as mp
# from mediapipe import *
import cv2
import numpy as np
import os.path
import mysql.connector as msc
from google.protobuf.json_format import MessageToDict
from prettytable import PrettyTable
import subprocess
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from matplotlib import *
# import os

import db_conn
import sys
import tkinter_demo as tkdemo
from Signup import *
import Dashboard


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)


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

        # frame_login = tk.Frame(main_frame, bg="dark blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        # frame_login.place(rely=0.30, relx=0.17, height=200, width=420)
        def only_numbers(char):
            return char.isdigit()
        validation = main_frame.register(only_numbers)

        lb0 = Label(main_frame, text="Patient Category", width=20,
                    font=("Verdana", 12), background="#9EAABF")
        lb0.place(x=20, y=60)
        options = ['C', 'J']
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(main_frame, clicked, *options)
        drop.place(x=240, y=60)

        lb1 = Label(main_frame, text="Patient Id", width=20,
                    font=("Verdana", 12), background="#9EAABF")
        lb1.place(x=20, y=100)
        en1 = Entry(main_frame, width=15, validate="key",
                    validatecommand=(validation, '%S'))
        en1.place(x=240, y=100)

        # , validate="key", validatecommand=(validation, '%S')
        # lb3= Label(main_frame, text="Enter Password", width=20, font=("Verdana",12))
        # lb3.place(x=20, y=140)
        # en3= Entry(main_frame, show="*")
        # en3.place(x=240, y=140)

        Button(main_frame, text="Login", width=15, command=lambda: getlogin(
        ), background="#9EAABF").place(x=150, y=200)
        # Button(main_frame, text="Register", width=15, command=lambda: get_signup()).place(x=300,y=200)

        def get_signup(Patient_Id):
            SignupPage(Patient_Id)
            # SignupPage()

        def getlogin():
            Patient_id = clicked.get()+str(en1.get())
            # password = en3.get()
            # print(Patient_id)

            validation = validate(Patient_id)
            if validation:
                
                LoginPage.destroy(self)
                Dashboard.Dashboard(Patient_id)
                top.withdraw()
                # SignupPage.top.deiconify()
                # LoginPage.top.deiconify()
                # LoginPage.destroy(self)
                # root.deiconify()          #commented
                # tkdemo.top.destroy()
                # top.destroy()
            else:
                # tk.messagebox.showerror("Information", "The Patient_Id or Password you have entered are incorrect ")
                LoginPage.destroy(self)
                get_signup(Patient_id)

        def validate(Patient_id):
            # Checks the text file for a Patient_Id/password combination.
            try:
                query = f"Select * from patients where Patient_ID='{Patient_id}'"

                # print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchall()
                if (len(row) == 1):
                    return True
                else:
                    return False

            except ConnectionError:
                # print("You need to Register first or amend Line 71 to if True:")
                return False
            
        db_conn.mydb.commit()


top = LoginPage()
top.title("Login Page")
top.mainloop()

top.destroy()
