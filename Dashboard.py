import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from prettytable import PrettyTable
import subprocess
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
        
        lb2 = Label(main_frame, text=uname, width=15, height=2, font=("Verdana",12), background="blue")
        lb2.place(x=600, y=60)
        
        # lb3 = Label(main_frame, text="Record", width=10, font=("Verdana",10))
        # lb3.place(x=30,y=140)
        
        Button(main_frame, text="Record", width=18, command=lambda: run_script()).place(x=600,y=150) 
        
        # table = PrettyTable(['Subject Code', 'Subject', 'Marks'])
        # print(table)
        
        Button(main_frame, text="List Angles", width=18, command=lambda: list_angles()).place(x=20,y=50) 
        
    
        def run_script():
            # subprocess.call(['python', f'hcd.py',f'{user_id}'])
            subprocess.call(["python",'hcd.py',f"{user_id}"])
            
            # os.system(f"hcd.py {user_id}")
            
        
        def list_angles():
            ang_label = Label(main_frame,text='L PIP', width=5)
            ang_label.place(x=20, y=100)
            ang_label = Label(main_frame,text='L DIP', width=5)
            ang_label.place(x=80, y=100)
            ang_label = Label(main_frame,text='L MCP', width=5)
            ang_label.place(x=140, y=100)
            ang_label = Label(main_frame,text='R PIP', width=5)
            ang_label.place(x=200, y=100)
            ang_label = Label(main_frame,text='R DIP', width=5)
            ang_label.place(x=260, y=100)
            ang_label = Label(main_frame,text='R MCP', width=5)
            ang_label.place(x=320, y=100)
            print("Angles")
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
            # cnt=1
            # for ang in row:
            #     # print(ang)
            #     for y in range(len(ang)):
            #         ang_label = Label(main_frame,text=ang[y], width=5)
            #         ang_label.place(x=20+(60*y), y=100+(40*cnt))
                    
                
                
                
                # ang_label = Label(main_frame,text=ang[1], width=5)
                # ang_label.place(x=20+(25*r), y=100+(40*cnt))
                # r=r+1
                # ang_label = Label(main_frame,text=ang[2], width=5)
                # ang_label.place(x=20+(25*r), y=100+(40*cnt))
                # ang_label.pack()
                # cnt=cnt+1
        
        
# top = Dashboard()
# top.title("Dashboard")
# top.mainloop()

# top.destroy()