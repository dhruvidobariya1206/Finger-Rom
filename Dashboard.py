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
# from matplotlib import *
# import os

import db_conn
import tkinter_demo as tkdemo
import Signup
# import Login
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
        
        # lg = LoginPage()
       
    
        # print()
        # print()
        # print()
        # print(uname)
        # print()
        # print()
        # print()
        
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
            ang_label1 = Label(main_frame,text='Finger', width=10)
            ang_label1.place(x=20, y=100)
            ang_label2 = Label(main_frame,text='PIP', width=10)
            ang_label2.place(x=120, y=100)
            ang_label3 = Label(main_frame,text='DIP', width=10)
            ang_label3.place(x=220, y=100)
            ang_label4 = Label(main_frame,text='MCP', width=10)
            ang_label4.place(x=320, y=100)
            
            fin_label1 = Label(main_frame,text='Index', width=10)
            fin_label1.place(x=20, y=140)
            fin_label2 = Label(main_frame,text='Middle', width=10)
            fin_label2.place(x=20, y=180)
            fin_label3 = Label(main_frame,text='Ring', width=10)
            fin_label3.place(x=20, y=220)
            fin_label4 = Label(main_frame,text='Little', width=10)
            fin_label4.place(x=20, y=260)
            fin_label5 = Label(main_frame,text='Thumb', width=10)
            fin_label5.place(x=20, y=300)
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
            
            # x=['index','middle','ring','little','thumb']
            # plt.plot(x,prev_pip,label="Prev PIP", marker="o", linestyle = 'dashed',c = '#4CAF50')
            # plt.plot(x,curr_pip, label="curr PIP", marker="o",c = '#4CAF50')
            # plt.plot(x,prev_tip,label="Prev TIP", marker="o", linestyle = 'dashed',c = '#AAAF50')
            # plt.plot(x,curr_tip, label="curr TIP", marker="o",c = '#AAAF50')
            # plt.plot(x,prev_mcp,label="Prev MCP", marker="o", linestyle = 'dashed',c = '#4CAFAA')
            # plt.plot(x,curr_mcp, label="curr MCP", marker="o",c = '#4CAFAA')
            # plt.xlabel("Finger")
            # plt.ylabel("Angle Measure")
            # plt.title('Progress')
            # plt.legend(loc='upper right')
            # plt.show()
            
            # # creating the Tkinter canvas
            # # containing the Matplotlib figure
            # canvas = FigureCanvasTkAgg(fig,master = top)  
            # canvas.draw()
  
            # # placing the canvas on the Tkinter window
            # canvas.get_tk_widget().pack()
  
            # # creating the Matplotlib toolbar
            # toolbar = NavigationToolbar2Tk(canvas,top)
            # toolbar.update()
  
            # # placing the toolbar on the Tkinter window
            # canvas.get_tk_widget().pack()
            
            tip=[]
            pip=[]
            mcp=[]
            for i in range(5):
                col1=[]
                col1.append(prev_tip[i])
                col1.append(curr_tip[i])
                tip.append(col1)
    
                col2=[]
                col2.append(prev_pip[i])
                col2.append(curr_pip[i])
                pip.append(col2)

                col3=[]
                col3.append(prev_tip[i])
                col3.append(curr_tip[i])
                mcp.append(col3)
            
            lbl=['index','middle','ring','little','thumb']
            x=['previous','current']
            
            figure1 = plt.Figure(figsize=(6, 5), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, top)
            bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            # df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
            # df1.plot(kind='bar', legend=True, ax=ax1)
            for i in range(5):
                ax1.plot(x, tip[i], label=f"{lbl[i]}", marker="o")
            ax1.xlabel("Progress")
            ax1.ylabel("Angle Measure")
            ax1.title('Progress')
            ax1.legend(loc='upper right')
            ax1.show() 
            # ax1.set_title('Country Vs. GDP Per Capita')

            
# top = Dashboard("dhruvi","9876543210")
# top.title("Dashboard")
# top.mainloop()

# top.destroy()