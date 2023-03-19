import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
from Signup import *
import Dashboard






class LoginPage(tk.Tk):

    def __init__(self,*args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # self.user=user 
        # self.phone=phone
        
        main_frame = tk.Frame(self, bg="#1c4966", height=450, width=300)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("450x300")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}

        # frame_login = tk.Frame(main_frame, bg="dark blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        # frame_login.place(rely=0.30, relx=0.17, height=200, width=420)
        def only_numbers(char):
            return char.isdigit()
        validation = main_frame.register(only_numbers)

        lb1= Label(main_frame, text="Enter Patient Id", width=20, font=("Verdana",12), background="#9EAABF")  
        lb1.place(x=20, y=60) 
        options=['C','J']
        clicked = StringVar()
        clicked.set(options[0])
        drop = OptionMenu(main_frame, clicked, *options)
        drop.place(x=240, y=60)
        en1= Entry(main_frame, validate="key", validatecommand=(validation, '%S'))  
        en1.place(x=280, y=60)
        
        lb2= Label(main_frame, text="Enter Phone Number", width=20, font=("Verdana",12), background="#9EAABF")  
        lb2.place(x=20, y=100)  
        en2= Entry(main_frame, validate="key", validatecommand=(validation, '%S'))  
        en2.place(x=240, y=100) 
        # , validate="key", validatecommand=(validation, '%S')
        # lb3= Label(main_frame, text="Enter Password", width=20, font=("Verdana",12))  
        # lb3.place(x=20, y=140)  
        # en3= Entry(main_frame, show="*")  
        # en3.place(x=240, y=140)  

        Button(main_frame, text="Login", width=15, command=lambda: getlogin(), background="#9EAABF").place(x=150,y=200) 
        # Button(main_frame, text="Register", width=15, command=lambda: get_signup()).place(x=300,y=200) 
        
        
        
        def get_signup(Patient_Id, phone):
            SignupPage(Patient_Id,phone)
            # SignupPage()

        def getlogin():
            Patient_id = clicked.get()+str(en1.get())
            # password = en3.get()
            print(Patient_id)
            number = en2.get()
            if(len(number)!=10):
                tk.messagebox.showerror("Invalid Number", "Please enter a valid number")
            else:
                validation = validate(Patient_Id, number)
                if validation:
                    
                    LoginPage.destroy(self)
                    Dashboard.Dashboard(Patient_Id, number)
                    
                    # SignupPage.top.deiconify()
                    # LoginPage.top.deiconify()
                    # LoginPage.destroy(self)
                    top.withdraw()
                    # root.deiconify()          #commented
                    # tkdemo.top.destroy()
                    # top.destroy()
                else:
                    # tk.messagebox.showerror("Information", "The Patient_Id or Password you have entered are incorrect ")
                    LoginPage.destroy(self)
                    get_signup(Patient_Id,number)

        def validate(Patient_Id, number):
            # Checks the text file for a Patient_Id/password combination.
            try:
                query = "Select * from patients where Patient_ID='"+Patient_Id+"' and PPhone='"+number+"'"
                
                # print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchall()
                if(len(row)==1):
                    return True
                else:
                    return False
                
            except ConnectionError:
                # print("You need to Register first or amend Line 71 to if True:")
                return False



top = LoginPage()
top.title("Login Page")
top.mainloop()

top.destroy()