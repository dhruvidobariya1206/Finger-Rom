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

import db_conn
import tkinter_demo as tkdemo
from msgBox import msgBox
import Login
import History
# from Login import *


# from hcd import *
# user = Login.getlogin.username
# print(user)

selected_hand = ''

# ########################################################################################################

# ########################################################################################################



class Dashboard(tk.Tk):
    def __init__(self, Patient_Id, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        query = f"Select * from patients where Patient_ID='{Patient_Id}'"
        # print(query)
        db_conn.mycursor.execute(query)
        patient_details = db_conn.mycursor.fetchone()
        user_id = patient_details[0]
        
        
        
        main_frame = tk.Frame(self, bg="#9EAABF", height=700, width=800)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        
        self.geometry("1200x750")  # Sets window size to 626w x 431h pixels
          # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}
        
        
        lb1= Label(main_frame, text=f"{patient_details[1]} {patient_details[2]} {patient_details[3]}", width=70, height=1, font=("Verdana",22), foreground='#FFFFFF', background="#1c4966")  
        lb1.place(x=0, y=0)
        
         
        
        # lb2 = Label(main_frame, text=Patient_Id, width=15, height=2, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966")
        # lb2.place(x=0, y=0)
        
        logout = Button(main_frame, text="Logout", width=15, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: logout())
        logout.place(x=1000, y=50)
        # lb3 = Label(main_frame, text="Record", width=10, font=("Verdana",10))
        # lb3.place(x=30,y=140)
        
        Button(main_frame, text="Record", width=18, command=lambda: run_script()).place(x=50,y=70) 
        
        Button(main_frame, text="List Angles", width=18, command=lambda: list_angles()).place(x=50,y=120)
        
        Button(main_frame, text="Veiw Progress", width=18, command=lambda: view_progress()).place(x=50,y=170) 
        
        Button(main_frame, text="Veiw History", width=18, command=lambda: history()).place(x=50,y=220) 
        
        # search_entry=Entry(main_frame, text="Search", width=10, font=("Verdana",18))
        # search_entry.place(x=900, y=70)
        # search_entry.insert(0,'Search')
        # search_icon = tk.PhotoImage(file="search_icon.png")
        # search_btn = Button(main_frame, image=search_icon, command=lambda: search())
        # search_btn.place(x=100,y=70)
        # Button(main_frame, text="Search", width=10, command=lambda: search()).place(x=1060,y=70) 
        
        def history():
            Dashboard.destroy(self)
            top = History.History(user_id)
            top.title("History")
            top.mainloop()
            
    
        def run_script():
            # subprocess.call(['python', f'hcd.py',f'{user_id}'])
            subprocess.call(["python",'hcd.py',f"{user_id}"])
            list_angles()
            view_progress()
            
        
        def logout():
            # print("search") 
            response = messagebox.askokcancel("Logout", "Are you sure you want to logout?")
            if response:
                Dashboard.destroy(self)
                top = Login.LoginPage()
                top.title("Login Page")
                top.mainloop()
                
            # LoginPage()   
            # Dashboard.destroy(self)
            
        

    # Get the selected option
            # return hand.get()
        
        
        def list_angles():
            # hand = tk.simpledialog.askstring("Input", "Enter hand:")
            # hand = hand[0].upper() + hand[1:]
            
            dialog_window = tk.Toplevel(self)
            dialog = msgBox(dialog_window)
            hand = dialog.show()
            # print(f"hand={hand}")
            # Update the main window with the selected hand value
            # lb_hand = Label(main_frame, text=hand, width=8, font=("Verdana",22), foreground='#FFFFFF', background="#1c4966")
            # lb_hand.place(x=1000,y=100)

            
                
            
            lb1.config(text=f"{patient_details[1]} {patient_details[2]} {patient_details[3]} - {hand.lower()} hand")
            
            # ang_label1 = Label(main_frame,text='Sr No.', width=10)
            # ang_label1.place(x=20, y=100)
            ang_label1 = Label(main_frame,text='Finger', width=10)
            ang_label1.place(x=350, y=70)
            ang_label2 = Label(main_frame,text='PIP', width=10)
            ang_label2.place(x=450, y=70)
            ang_label3 = Label(main_frame,text='DIP', width=10)
            ang_label3.place(x=550, y=70)
            ang_label4 = Label(main_frame,text='MCP', width=10)
            ang_label4.place(x=650, y=70)
            
            fin_label1 = Label(main_frame,text='Index', width=10)
            fin_label1.place(x=350, y=110)
            fin_label2 = Label(main_frame,text='Middle', width=10)
            fin_label2.place(x=350, y=150)
            fin_label3 = Label(main_frame,text='Ring', width=10)
            fin_label3.place(x=350, y=190)
            fin_label4 = Label(main_frame,text='Little', width=10)
            fin_label4.place(x=350, y=230)
            fin_label5 = Label(main_frame,text='Thumb', width=10)
            fin_label5.place(x=350, y=270)
            # print("Angles")
            query1 = f"Select * from angle_pip where P_id='{user_id}' and Hand_Side='{hand}' ORDER BY SrNo DESC LIMIT 1;"
            # print(query1)
            db_conn.mycursor.execute(query1)
            db_conn.mydb.commit()
            
            row1 = db_conn.mycursor.fetchone()
            
            
            query2 = f"Select * from angle_tip where P_id='{user_id}' and Hand_Side='{hand}' ORDER BY SrNo DESC LIMIT 1;"
            # print(query2)
            db_conn.mycursor.execute(query2)
            db_conn.mydb.commit()
            row2 = db_conn.mycursor.fetchone()

            query3 = f"Select * from angle_mcp where P_id='{user_id}' and Hand_Side='{hand}' ORDER BY SrNo DESC LIMIT 1;"
            # print(query3)
            db_conn.mycursor.execute(query3)
            db_conn.mydb.commit()
            row3 = db_conn.mycursor.fetchone()
            
            if(len(row1)==0 or len(row2)==0 or len(row3)==0):
                for ang in range(5):
                # num = Label(main_frame, text='111', widht=10)
                # num.place(x=20,y=140+(40*ang))
                    if(ang==4):
                        value1 = Label(main_frame,text="0", width=22)
                        value1.place(x=450, y=110+(40*ang))
                        value3 = Label(main_frame,text="0", width=10)
                        value3.place(x=650, y=110+(40*ang))
                        break
                    
                    value1 = Label(main_frame,text="0", width=10)
                    value1.place(x=450, y=110+(40*ang))
                
                    value2 = Label(main_frame,text="0", width=10)
                    value2.place(x=550, y=110+(40*ang))
                
                    value3 = Label(main_frame,text="0", width=10)
                    value3.place(x=650, y=110+(40*ang))
                
            else:
                for ang in range(5):
                    # num = Label(main_frame, text='111', widht=10)
                    # num.place(x=20,y=140+(40*ang))
                    if(ang==4):
                        value1 = Label(main_frame,text=row1[4+ang], width=22)
                        value1.place(x=450, y=110+(40*ang))
                        value3 = Label(main_frame,text=row3[4+ang], width=10)
                        value3.place(x=650, y=110+(40*ang))
                        break
                        
                    value1 = Label(main_frame,text=row1[4+ang], width=10)
                    value1.place(x=450, y=110+(40*ang))
                    
                    value2 = Label(main_frame,text=row2[4+ang], width=10)
                    value2.place(x=550, y=110+(40*ang))
                    
                    value3 = Label(main_frame,text=row3[4+ang], width=10)
                    value3.place(x=650, y=110+(40*ang))
                        
        def view_progress():
            # print("View Progress")
            # hand = tk.simpledialog.askstring("Input", "Enter hand:")
            # hand = hand[0].upper() + hand[1:]
            
            dialog_window = tk.Toplevel(self)
            dialog = msgBox(dialog_window)
            hand = dialog.show()
            # print(hand)
            # print(f'hand_ {hand}')
            fig = Figure(figsize = (5,5), dpi = 100)
            lb1.config(text=f"{patient_details[1]} {patient_details[2]} {patient_details[3]} - {hand} hand")
            # plot1 = fig.add_subplot(111)
            
            query1 = f"Select ind, mid, ring, little, thumb from angle_pip where P_id='{user_id}' and Hand_Side='{hand}';"
            # print(query1)
            db_conn.mycursor.execute(query1)
            db_conn.mydb.commit()
            row1 = db_conn.mycursor.fetchall()
            
            query2 = f"Select ind, mid, ring, little, thumb from angle_tip where P_id='{user_id}' and Hand_Side='{hand}';"
            # print(query1)
            db_conn.mycursor.execute(query2)
            row2 = db_conn.mycursor.fetchall()
            db_conn.mydb.commit()

            query3 = f"Select ind, mid, ring, little, thumb from angle_mcp where P_id='{user_id}' and Hand_Side='{hand}';"
            # print(query1)
            db_conn.mycursor.execute(query3)
            row3 = db_conn.mycursor.fetchall()
            db_conn.mydb.commit()
            
            
            if(len(row1)==0 or len(row2)==0 or len(row3)==0):
                tk.messagebox.showinfo("Alert",f"Please record the angles for {hand} hand")
            
            else:
                dip=[]
                pip=[]
                mcp=[]
                
                for data in row1:
                    pip.append(data)
                for data in row2:
                    dip.append(data)
                for data in row3:
                    mcp.append(data)
            
                dip = pd.DataFrame(dip)
                pip = pd.DataFrame(pip)
                mcp = pd.DataFrame(mcp)
                
                lbl = ['index','middle','ring','little','thumb']
                
                figure1 = plt.Figure(figsize=(3.75, 3.75), dpi=100)
                
                graph_tip = figure1.add_subplot(1,1,1)
                graph_tip.set_ylabel('Angle Measure')
                graph_tip.set_xlabel('Progress')
                # graph_tip.set_legend(loc="bottom right")
                line1 = FigureCanvasTkAgg(figure1, main_frame)
                line1.get_tk_widget().place(x=20,y=350)
                for i in range(5):
                    dip[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_tip, marker="o")
                graph_tip.set_title("DIP")
                
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
                    mcp[i].plot(kind='line', label=f"{lbl[i]}", legend=True, ax=graph_mcp, marker="o")
                graph_mcp.set_title("MCP")
                
                
            # print("End")
        db_conn.mydb.commit() 
        # main_frame.destroy()
            
            
# top = Dashboard("dhruvi","9876543210")
# top.title("Dashboard")
# top.mainloop()

# top.destroy()