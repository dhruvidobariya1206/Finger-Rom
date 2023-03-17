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
        
        main_frame = tk.Frame(self, bg="#9EAABF", height=450, width=300)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("450x300")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "dark blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "dark blue",
                       "foreground": "#EEFFFF"}

        # frame_login = tk.Frame(main_frame, bg="dark blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        # frame_login.place(rely=0.30, relx=0.17, height=200, width=420)

        lb1= Label(main_frame, text="Enter Name", width=20, font=("arial",12))  
        lb1.place(x=20, y=60)  
        en1= Entry(main_frame)  
        en1.place(x=240, y=60)
        
        lb2= Label(main_frame, text="Enter Phone Number", width=20, font=("arial",12))  
        lb2.place(x=20, y=100)  
        en2= Entry(main_frame)  
        en2.place(x=240, y=100) 
        # , validate="key", validatecommand=(validation, '%S')
        # lb3= Label(main_frame, text="Enter Password", width=20, font=("arial",12))  
        # lb3.place(x=20, y=140)  
        # en3= Entry(main_frame, show="*")  
        # en3.place(x=240, y=140)  

        Button(main_frame, text="Login", width=15, command=lambda: getlogin()).place(x=150,y=200) 
        # Button(main_frame, text="Register", width=15, command=lambda: get_signup()).place(x=300,y=200) 
        
        def get_signup(username, phone):
            SignupPage(username,phone)
            # SignupPage()

        def getlogin():
            username = en1.get()
            # password = en3.get()
            number = en2.get()
            print()
            print(type(number))
            print()
            
            # if your want to run the script as it is set validation = True
            validation = validate(username, number)
            if validation and len(number)==10:
                # tk.messagebox.showinfo("Login Successful",
                                    #    "Welcome {}".format(username))
                # user = username
                # phone = number
                # print()
                # print()
                # print()
                # print(user)
                # print()
                # print()
                # print()
                LoginPage.destroy(self)
                Dashboard.Dashboard(username, number)
                
                # SignupPage.top.deiconify()
                # LoginPage.top.deiconify()
                # LoginPage.destroy(self)
                top.withdraw()
                # root.deiconify()          #commented
                # tkdemo.top.destroy()
                # top.destroy()
            else:
                # tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")
                get_signup(username,number)

        def validate(username, number):
            # Checks the text file for a username/password combination.
            try:
                query = "Select * from patients where PName='"+username+"' and PPhone='"+number+"'"
                
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