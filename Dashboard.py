import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
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
import tkinter_demo as tkdemo
import Signup
import Login as lg
from Login import *


# from hcd import *
# user = Login.getlogin.username
# print(user)

class Dashboard(tk.Tk):
    def __init__(self, uname, phone, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        query = "Select PId from patients where PPhone ='"+phone+"' and PName='"+uname+"'"
        print(query)
        db_conn.mycursor.execute(query)
        row = db_conn.mycursor.fetchone()
        user_id = row[0]
        
        
        
        main_frame = tk.Frame(self, bg="#8D99AE", height=700, width=800)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        
        self.geometry("1200x750")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}
        
        
        lb1= Label(main_frame, text="", width=800, font=("Verdana",20), background="dark blue")  
        lb1.place(x=0, y=0)
        
        Button(main_frame, text="List Angles", width=18, command=lambda: list_angles()).place(x=20,y=50) 
        
        lb2 = Label(main_frame, text=uname, width=15, height=2, font=("Verdana",12), background="blue")
        lb2.place(x=600, y=60)
        
        # lb3 = Label(main_frame, text="Record", width=10, font=("Verdana",10))
        # lb3.place(x=30,y=140)
        
        Button(main_frame, text="Record", width=18, command=lambda: run_script()).place(x=600,y=150) 
        
        Button(main_frame, text="Veiw Progress", width=18, command=lambda: view_progress()).place(x=600,y=240) 
        
    
        def run_script():
            # subprocess.call(['python', f'hcd.py',f'{user_id}'])
            subprocess.call(["python",'hcd.py',f"{user_id}"])
            
            
            
        
        def list_angles():
            ang_label1 = Label(main_frame,text='Sr No.', width=10)
            ang_label1.place(x=20, y=100)
            ang_label1 = Label(main_frame,text='Finger', width=10)
            ang_label1.place(x=120, y=100)
            ang_label2 = Label(main_frame,text='PIP', width=10)
            ang_label2.place(x=220, y=100)
            ang_label3 = Label(main_frame,text='DIP', width=10)
            ang_label3.place(x=320, y=100)
            ang_label4 = Label(main_frame,text='MCP', width=10)
            ang_label4.place(x=420, y=100)
            
            fin_label1 = Label(main_frame,text='Index', width=10)
            fin_label1.place(x=120, y=140)
            fin_label2 = Label(main_frame,text='Middle', width=10)
            fin_label2.place(x=120, y=180)
            fin_label3 = Label(main_frame,text='Ring', width=10)
            fin_label3.place(x=120, y=220)
            fin_label4 = Label(main_frame,text='Little', width=10)
            fin_label4.place(x=120, y=260)
            fin_label5 = Label(main_frame,text='Thumb', width=10)
            fin_label5.place(x=120, y=300)
            # print("Angles")
            query1 = f"Select * from angle_pip where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 1;"
            print(query1)
            db_conn.mycursor.execute(query1)
            row1 = db_conn.mycursor.fetchone()
            
            query2 = f"Select * from angle_tip where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 1;"
            print(query2)
            db_conn.mycursor.execute(query2)
            row2 = db_conn.mycursor.fetchone()
            
            query3 = f"Select * from angle_mcp where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 1;"
            print(query3)
            db_conn.mycursor.execute(query3)
            row3 = db_conn.mycursor.fetchone()
            
            for ang in range(5):
                num = Label(main_frame, text="111", widht=10)
                num.place(x=20,y=140+(40*ang))
                
                value1 = Label(main_frame,text=row1[2+ang], width=10)
                value1.place(x=120, y=140+(40*ang))
                
                value2 = Label(main_frame,text=row2[2+ang], width=10)
                value2.place(x=220, y=140+(40*ang))
                
                value3 = Label(main_frame,text=row3[2+ang], width=10)
                value3.place(x=320, y=140+(40*ang))
                    
        def view_progress():
            print("View Progress")
            fig = Figure(figsize = (5,5), dpi = 100)
            
            plot1 = fig.add_subplot(111)
            
            query1 = f"Select ind, mid, ring, little, thumb from angle_pip where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 2;"
            # print(query1)
            db_conn.mycursor.execute(query1)
            row1 = db_conn.mycursor.fetchall()

            query2 = f"Select ind, mid, ring, little, thumb from angle_tip where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 2;"
            # print(query1)
            db_conn.mycursor.execute(query2)
            row2 = db_conn.mycursor.fetchall()

            query2 = f"Select ind, mid, ring, little, thumb from angle_mcp where P_id='{user_id}' ORDER BY SrNo DESC LIMIT 2;"
            # print(query1)
            db_conn.mycursor.execute(query2)
            row3 = db_conn.mycursor.fetchall()
            
            # if(row1.ro)
            
            prev_pip=np.array(row1[1])
            curr_pip=np.array(row1[0])
            prev_tip=np.array(row2[1])
            curr_tip=np.array(row2[0])
            prev_mcp=np.array(row3[1])
            curr_mcp=np.array(row3[0])
            
            tip=[]
            pip=[]
            mcp=[]
                
            col11=[]
            col21=[]
            col31=[]
            # col.append
            for j in range(5):
                col11.append(prev_tip[j])
                col21.append(prev_pip[j])
                col31.append(prev_mcp[j])
            tip.append(col11)
            pip.append(col21)
            mcp.append(col31)
            
            col12=[]
            col22=[]
            col32=[]
            # col.append
            for j in range(5):
                col12.append(curr_tip[j])
                col22.append(curr_pip[j])
                col32.append(curr_mcp[j])
            tip.append(col12)
            pip.append(col22)
            mcp.append(col32)
            
            tip=pd.DataFrame(tip)
            pip = pd.DataFrame(pip)
            mcp = pd.DataFrame(mcp)
            
            print(pip)
            print(tip)
            print(mcp)
            
            lbl=['index','middle','ring','little','thumb']
            x=['previous','current']
            
            figure1 = plt.Figure(figsize=(3.75, 3.75), dpi=100)
            
            graph_tip = figure1.add_subplot(1,1,1)
            graph_tip.set_ylabel('Angle Measure')
            graph_tip.set_xlabel('Progress')
            # graph_tip.set_legend(loc="bottom right")
            line1 = FigureCanvasTkAgg(figure1, main_frame)
            line1.get_tk_widget().place(x=20,y=350)
            for i in range(5):
                tip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_tip, marker="o")
            graph_tip.set_title("TIP")
            
            figure2 = plt.Figure(figsize=(3.75, 3.75), dpi=100)
            graph_pip = figure2.add_subplot(1,1,1)
            graph_pip.set_ylabel('Angle Measure')
            graph_pip.set_xlabel('Progress')
            line1 = FigureCanvasTkAgg(figure2, main_frame)
            line1.get_tk_widget().place(x=415,y=350)
            for i in range(5):
                pip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_pip, marker="o")
            graph_pip.set_title("PIP")
            
            figure3 = plt.Figure(figsize=(3.75, 3.75), dpi=100)
            graph_mcp = figure3.add_subplot(1,1,1)
            graph_mcp.set_ylabel('Angle Measure')
            graph_mcp.set_xlabel('Progress')
            line1 = FigureCanvasTkAgg(figure3, main_frame)
            line1.get_tk_widget().place(x=810,y=350)
            for i in range(5):
                tip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_mcp, marker="o")
            graph_mcp.set_title("MCP")
            
            
            print("End")
            
            
top = Dashboard("dhruvi","9876543210")
top.title("Dashboard")
top.mainloop()

top.destroy()