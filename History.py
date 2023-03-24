import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
from Signup import *
import Dashboard


class History(tk.Tk):

    def __init__(self, user_id, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # self.user=user
        # self.phone=phone

        # this is the background
        main_frame = tk.Frame(self, bg="#9EAABF", height=450, width=300)
        main_frame.pack(fill="both", expand="true")

        self.geometry("1200x750")  # Sets window size to 626w x 431h pixels
        # self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16),
                        "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}

        query = f"Select * from patients where Patient_ID='{user_id}'"
        # print(query)
        db_conn.mycursor.execute(query)
        patient_details = db_conn.mycursor.fetchone()
        
        lb1= Label(main_frame, text=f"{patient_details[1]} {patient_details[2]} {patient_details[3]}", width=57, height=1, font=("Verdana",22), foreground='#FFFFFF', background="#1c4966")  
        lb1.place(x=0, y=0)
        
        Button(main_frame, text="Left DIP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: DIP("Left")).place(x=20,y=60)
        Button(main_frame, text="Left PIP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: PIP("Left")).place(x=150,y=60)
        Button(main_frame, text="Left MCP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: MCP("Left")).place(x=280,y=60)
        Button(main_frame, text="Right DIP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: DIP("Right")).place(x=410,y=60)
        Button(main_frame, text="Right PIP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: PIP("Right")).place(x=540,y=60)
        Button(main_frame, text="Right MCP", width=10, font=("Verdana",12), foreground='#FFFFFF', background="#1c4966", command=lambda: MCP("Right")).place(x=670,y=60)
        
        
        Button(main_frame, text="Back", width=15, font=("Verdana",14), foreground='#FFFFFF', background="#1c4966", command=lambda: back()).place(x=1025,y=0)
        
        def back():
            History.destroy(self)
            Dashboard.Dashboard(user_id)
            
        def DIP(hand):
            # print("DIP"+hand)
            query1 = f"Select * from angle_tip where P_id = '{user_id}' and Hand_Side = '{hand}'"
            # print(query1)
            db_conn.mycursor.execute(query1)
            row1 = db_conn.mycursor.fetchall()
            
            if(len(row1)==0):
                tk.messagebox.showinfo("Alert",f"Please record the angles for {hand} hand")
            else:
                ang_label1 = Label(main_frame,text='Finger/Date', width=10, foreground='#FFFFFF', background="#1c4966")
                ang_label1.place(x=30, y=150)
                
                fin_label1 = Label(main_frame,text='Index', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label1.place(x=30, y=190)
                fin_label2 = Label(main_frame,text='Middle', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label2.place(x=30, y=230)
                fin_label3 = Label(main_frame,text='Ring', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label3.place(x=30, y=270)
                fin_label4 = Label(main_frame,text='Little', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label4.place(x=30, y=310)
                fin_label5 = Label(main_frame,text='Thumb', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label5.place(x=30, y=350)
                cnt=0
                for data in row1:
                    # print(data)
                    ang_label2 = Label(main_frame,text=data[3], width=10, foreground='#FFFFFF', background="#1c4966")
                    ang_label2.place(x=130+100*cnt, y=150)
                    
                    value1 = Label(main_frame,text=data[4], width=10)
                    value1.place(x=130+100*cnt, y=190)
                
                    value2 = Label(main_frame,text=data[5], width=10)
                    value2.place(x=130+100*cnt, y=230)
                
                    value3 = Label(main_frame,text=data[6], width=10)
                    value3.place(x=130+100*cnt, y=270)
                    
                    value4 = Label(main_frame,text=data[7], width=10)
                    value4.place(x=130+100*cnt, y=310)
                    
                    value5 = Label(main_frame,text=data[8], width=10)
                    value5.place(x=130+100*cnt, y=350)
                    cnt+=1
        
        def PIP(hand):
            # print("PIP"+hand)
            query1 = f"Select * from angle_pip where P_id = '{user_id}' and Hand_Side = '{hand}'"
            # print(query1)
            db_conn.mycursor.execute(query1)
            row1 = db_conn.mycursor.fetchall()
            
            if(len(row1)==0):
                tk.messagebox.showinfo("Alert",f"Please record the angles for {hand} hand")
            else:
                ang_label1 = Label(main_frame,text='Finger/Date', width=10, foreground='#FFFFFF', background="#1c4966")
                ang_label1.place(x=30, y=150)
                
                fin_label1 = Label(main_frame,text='Index', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label1.place(x=30, y=190)
                fin_label2 = Label(main_frame,text='Middle', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label2.place(x=30, y=230)
                fin_label3 = Label(main_frame,text='Ring', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label3.place(x=30, y=270)
                fin_label4 = Label(main_frame,text='Little', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label4.place(x=30, y=310)
                fin_label5 = Label(main_frame,text='Thumb', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label5.place(x=30, y=350)
                cnt=0
                for data in row1:
                    # print(data)
                    ang_label2 = Label(main_frame,text=data[3], width=10, foreground='#FFFFFF', background="#1c4966")
                    ang_label2.place(x=130+100*cnt, y=150)
                    
                    value1 = Label(main_frame,text=data[4], width=10)
                    value1.place(x=130+100*cnt, y=190)
                
                    value2 = Label(main_frame,text=data[5], width=10)
                    value2.place(x=130+100*cnt, y=230)
                
                    value3 = Label(main_frame,text=data[6], width=10)
                    value3.place(x=130+100*cnt, y=270)
                    
                    value4 = Label(main_frame,text=data[7], width=10)
                    value4.place(x=130+100*cnt, y=310)
                    
                    value5 = Label(main_frame,text=data[8], width=10)
                    value5.place(x=130+100*cnt, y=350)
                    cnt+=1
        
        
        def MCP(hand): 
            # print("MCP"+hand) 
            query1 = f"Select * from angle_mcp where P_id = '{user_id}' and Hand_Side = '{hand}'"
            # print(query1)
            db_conn.mycursor.execute(query1)
            row1 = db_conn.mycursor.fetchall()
            
            if(len(row1)==0):
                tk.messagebox.showinfo("Alert",f"Please record the angles for {hand} hand")
            else:
                ang_label1 = Label(main_frame,text='Finger/Date', width=10, foreground='#FFFFFF', background="#1c4966")
                ang_label1.place(x=30, y=150)
                
                fin_label1 = Label(main_frame,text='Index', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label1.place(x=30, y=190)
                fin_label2 = Label(main_frame,text='Middle', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label2.place(x=30, y=230)
                fin_label3 = Label(main_frame,text='Ring', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label3.place(x=30, y=270)
                fin_label4 = Label(main_frame,text='Little', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label4.place(x=30, y=310)
                fin_label5 = Label(main_frame,text='Thumb', width=10, foreground='#FFFFFF', background="#1c4966")
                fin_label5.place(x=30, y=350)
                cnt=0
                for data in row1:
                    # print(data)
                    ang_label2 = Label(main_frame,text=data[3], width=10, foreground='#FFFFFF', background="#1c4966")
                    ang_label2.place(x=130+100*cnt, y=150)
                    
                    value1 = Label(main_frame,text=data[4], width=10)
                    value1.place(x=130+100*cnt, y=190)
                
                    value2 = Label(main_frame,text=data[5], width=10)
                    value2.place(x=130+100*cnt, y=230)
                
                    value3 = Label(main_frame,text=data[6], width=10)
                    value3.place(x=130+100*cnt, y=270)
                    
                    value4 = Label(main_frame,text=data[7], width=10)
                    value4.place(x=130+100*cnt, y=310)
                    
                    value5 = Label(main_frame,text=data[8], width=10)
                    value5.place(x=130+100*cnt, y=350)
                    cnt+=1
        db_conn.mydb.commit()

# top = History()
# top.title("History")
# top.mainloop()

# top.destroy()
