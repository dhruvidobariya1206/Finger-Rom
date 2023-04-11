import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk
from tkinter import *
# from prettytable import PrettyTable
import subprocess
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from matplotlib import *
# import os
from tkinter import Tk, StringVar, ttk
import pandas as pd

import db_conn
# import tkinter_demo as tkdemo
import Login

gender = ""


class RecordList(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#9EAABF", height=700, width=800)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("1200x750")
        # self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#8D99AE",
                       "foreground": "#8D99AE"}

        def only_numbers(char):
            return char.isdigit()
        validation = main_frame.register(only_numbers)

        lb1 = Label(main_frame, text="List Records", width=57, height=1, font=(
            "Verdana", 22), foreground='#FFFFFF', background="#1c4966")
        lb1.place(x=0, y=0)

        Button(main_frame, text="Back", width=15, font=("Verdana", 14), foreground='#FFFFFF',
               background="#1c4966", command=lambda: back()).place(x=1025, y=0)

        lb0 = Label(main_frame, text="Patient Id", width=10,
                    font=("Verdana", 12), background="#9EAABF")
        lb0.place(x=0, y=60)
        options = ['C', 'J']
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(main_frame, clicked, *options)
        drop.place(x=110, y=59)

        en1 = Entry(main_frame, width=10, validate="key",
                    validatecommand=(validation, '%S'))
        en1.place(x=180, y=62)

        lb0 = Label(main_frame, text="Hand", width=10,
                    font=("Verdana", 12), background="#9EAABF")
        lb0.place(x=0, y=120)
        options_hand = ['Left', 'Right']
        hand_value = StringVar()
        hand_value.set(options_hand[0])
        drop2 = OptionMenu(main_frame, hand_value, *options_hand)
        drop2.place(x=110, y=120)
        
        Button(main_frame, text="Clear", width=10, command=lambda: clear(),
               foreground='#FFFFFF', background="#1c4966").place(x=1000, y=62)

        Button(main_frame, text="View", width=10, command=lambda: view(),
               foreground='#FFFFFF', background="#1c4966").place(x=200, y=120)

        def back():
            RecordList.destroy(self)
            Login.LoginPage()

        def view():
            # print("view")
            if (str(en1.get()) == ""):
                tk.messagebox.showerror(
                    "Information", "Please Enter Patient Id")

            else:
                Patient_id = clicked.get()+str(en1.get())
                hand = hand_value.get()
                # print(Patient_id)
                query = f"Select * from patients where Patient_ID='{Patient_id}'"
                # print(query)
                # print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchone()
                # print(row[1])

                if (row != None):

                    lb1 = Label(main_frame, text=f"Name: {row[1]} {row[3]}", width=25, height=1, font=(
                        "Verdana", 12), foreground='#FFFFFF', background="#1c4966")
                    lb1.place(x=420, y=120)

                    lb2 = Label(main_frame, text=f"Number: {row[4]}", width=20, height=1, font=(
                        "Verdana", 12), foreground='#FFFFFF', background="#1c4966")
                    lb2.place(x=700, y=120)

                    lb2 = Label(main_frame, text=f"Age: {row[6]}", width=20, height=1, font=(
                        "Verdana", 12), foreground='#FFFFFF', background="#1c4966")
                    lb2.place(x=930, y=120)

                    pipquery = f"Select DATE(Time), ind, mid, ring, little, thumb from angle_pip where P_id = '{Patient_id}' and Hand_Side = '{hand}'"
                    dipquery = f"Select DATE(Time), ind, mid, ring, little, thumb from angle_tip where P_id = '{Patient_id}' and Hand_Side = '{hand}'"
                    mcpquery = f"Select DATE(Time), ind, mid, ring, little, thumb from angle_mcp where P_id = '{Patient_id}' and Hand_Side = '{hand}'"
                    # print(pipquery)
                    # print(dipquery)
                    # print(mcpquery)
                    db_conn.mycursor.execute(pipquery)
                    pip_details = db_conn.mycursor.fetchall()

                    db_conn.mycursor.execute(dipquery)
                    dip_details = db_conn.mycursor.fetchall()

                    db_conn.mycursor.execute(mcpquery)
                    mcp_details = db_conn.mycursor.fetchall()

                    angle_names = ['dip', 'pip', 'mcp']
                    fingers = ['index', 'middle', 'ring', 'little', 'thumb']
                    
                    for i in range(3):
                        angle_n = Label(main_frame, text=(angle_names[i]), width=35, foreground='#FFFFFF', background="#1c4966").place(
                            x=120+(i*350), y=200)
                        for j in range(5):
                            finger_name = Label(main_frame, text=fingers[j], width=5, foreground='#FFFFFF', background="#1c4966").place(
                            x=120+(i*350)+(j*60), y=250)

                    i = 0
                    for data in dip_details:
                        # print("1")
                        dip1 = Label(main_frame, text=str(data[0]), foreground='#FFFFFF', background="#1c4966").place(
                            x=20, y=300+(i*30))
                        dip2=Label(main_frame, text=str(data[1]), width=5).place(
                            x=120, y=300+(i*30))
                        dip3=Label(main_frame, text=str(data[2]), width=5).place(
                            x=180, y=300+(i*30))
                        dip4=Label(main_frame, text=str(data[3]), width=5).place(
                            x=240, y=300+(i*30))
                        dip5=Label(main_frame, text=str(data[4]), width=5).place(
                            x=300, y=300+(i*30))
                        dip6=Label(main_frame, text=str(data[5]), width=5).place(
                            x=360, y=300+(i*30))
                        i+=1
                        
                    i = 0
                    for data in pip_details:
                        # print("1")
                        # Label(main_frame, text=str(data[0])).place(
                        #     x=20, y=300+(i*30))
                        Label(main_frame, text=str(data[1]), width=5).place(
                            x=470, y=300+(i*30))
                        Label(main_frame, text=str(data[2]), width=5).place(
                            x=530, y=300+(i*30))
                        Label(main_frame, text=str(data[3]), width=5).place(
                            x=590, y=300+(i*30))
                        Label(main_frame, text=str(data[4]), width=5).place(
                            x=650, y=300+(i*30))
                        Label(main_frame, text=str(data[5]), width=5).place(
                            x=710, y=300+(i*30))
                        i+=1
                        
                    i = 0
                    for data in mcp_details:
                        print("1")
                        # Label(main_frame, text=str(data[0])).place(
                        #     x=20, y=300+(i*30))
                        Label(main_frame, text=str(data[1]), width=5).place(
                            x=820, y=300+(i*30))
                        Label(main_frame, text=str(data[2]), width=5).place(
                            x=880, y=300+(i*30))
                        Label(main_frame, text=str(data[3]), width=5).place(
                            x=940, y=300+(i*30))
                        Label(main_frame, text=str(data[4]), width=5).place(
                            x=1000, y=300+(i*30))
                        Label(main_frame, text=str(data[5]), width=5).place(
                            x=1060, y=300+(i*30))
                        i+=1
                      
                      
                        
                    if(len(pip_details)==0 or len(dip_details)==0 or len(mcp_details)==0):
                        tk.messagebox.showinfo("Alert","No values recorded")
            
                    else:
                        dip=[]
                        pip=[]
                        mcp=[]
                
                        for data in pip_details:
                            pip.append(data)
                        for data in dip_details:
                            dip.append(data)
                        for data in mcp_details:
                            mcp.append(data)
            
                        dip = pd.DataFrame(dip)
                        pip = pd.DataFrame(pip)
                        mcp = pd.DataFrame(mcp)
                
                        lbl = ['index','middle','ring','little','thumb']

                        fig = Figure(figsize = (5,5), dpi = 100)
                        # lb1.config(text=f"{patient_details[1]} {patient_details[2]} {patient_details[3]} - {hand} hand")
                        
                        figure1 = plt.Figure(figsize=(3.0, 3.0), dpi=100)
                
                        graph_tip = figure1.add_subplot(1,1,1)
                        graph_tip.set_ylabel('Angle Measure')
                        graph_tip.set_xlabel('Progress')
                        # graph_tip.set_legend(loc="bottom right")
                        line1 = FigureCanvasTkAgg(figure1, main_frame)
                        line1.get_tk_widget().place(x=120,y=400)
                        for i in range(5):
                            dip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_tip, marker="o")
                        graph_tip.set_title("DIP")
                
                        figure2 = plt.Figure(figsize=(3.0, 3.0), dpi=100)
                        graph_pip = figure2.add_subplot(1,1,1)
                        graph_pip.set_ylabel('Angle Measure')
                        graph_pip.set_xlabel('Progress')
                        line1 = FigureCanvasTkAgg(figure2, main_frame)
                        line1.get_tk_widget().place(x=470,y=400)
                        for i in range(5):
                            pip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_pip, marker="o")
                        graph_pip.set_title("PIP")
                
                        figure3 = plt.Figure(figsize=(3.0, 3.0), dpi=100)
                        graph_mcp = figure3.add_subplot(1,1,1)
                        graph_mcp.set_ylabel('Angle Measure')
                        graph_mcp.set_xlabel('Progress')
                        line1 = FigureCanvasTkAgg(figure3, main_frame)
                        line1.get_tk_widget().place(x=820,y=400)
                        for i in range(5):
                            mcp[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_mcp, marker="o")
                        graph_mcp.set_title("MCP")
            

                else:
                    tk.messagebox.showerror(
                        "Information", "Entered patient id is invalid")


# root = RecordList()
# root.title("Records Page")
# root.mainloop()
