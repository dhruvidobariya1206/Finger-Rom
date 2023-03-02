import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo

class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#8D99AE", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("500x500")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#8D99AE",
                       "foreground": "#8D99AE"}

        lb1= Label(main_frame, text="Enter Name", width=15, font=("arial",12))  
        lb1.place(x=20, y=120)  
        en1= Entry(main_frame)  
        en1.place(x=200, y=120)  
        
        # lb3= Label(main_frame, text="Enter Email", width=15, font=("arial",12))  
        # lb3.place(x=20, y=160)  
        # en3= Entry(main_frame)  
        # en3.place(x=200, y=160)  
        
        lb4= Label(main_frame, text="Contact Number", width=15,font=("arial",12))  
        lb4.place(x=20, y=160)  
        en4= Entry(main_frame)  
        en4.place(x=200, y=160)  
        
        lb5= Label(main_frame, text="Select Gender", width=15, font=("arial",12))  
        lb5.place(x=20, y=200)  
        gen = StringVar()  
        Radiobutton(main_frame, text="Male", padx=5,variable=vars, value='M').place(x=200, y=200)  
        Radiobutton(main_frame, text="Female", padx =10,variable=vars, value='F').place(x=280,y=200)  
        # Radiobutton(main_frame, text="others", padx=15, variable=vars, value=3).place(x=310,y=240)  
        
        list_of_grp = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")  
        cv = StringVar()  
        drplist= OptionMenu(main_frame, cv, *list_of_grp)  
        drplist.config(width=15)  
        cv.set("A+")  
        lb2= Label(main_frame, text="Select Blood Group", width=15,font=("arial",12))  
        lb2.place(x=20,y=240)  
        drplist.place(x=200, y=240)  
        
        lb6= Label(main_frame, text="Enter Password", width=15,font=("arial",12))  
        lb6.place(x=20, y=280)  
        en6= Entry(main_frame, show='*')  
        en6.place(x=200, y=280)  
        
        lb7= Label(main_frame, text="Re-Enter Password", width=15,font=("arial",12))  
        lb7.place(x=22, y=320)  
        en7 =Entry(main_frame, show='*')  
        en7.place(x=200, y=320)  
        
        Button(main_frame, text="Register", width=15, command=lambda: signup()).place(x=200,y=360) 





        # label_user = tk.Label(main_frame, text_styles, text="Username:")
        # label_user.grid(row=1, column=0)

        # label_number = tk.Label(main_frame, text_styles, text="Phone Number:")
        # label_number.grid(row=2, column=0)
        
        # label_grp = tk.Label(main_frame, text_styles, text="Blood Group:")
        # label_grp.grid(row=3, column=0)

        # label_pw = tk.Label(main_frame, text_styles, text="Password:")
        # label_pw.grid(row=4, column=0)
        
        # entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        # entry_user.grid(row=1, column=1)
        
        # entry_number = ttk.Entry(main_frame, width=20, cursor="xterm")
        # entry_number.grid(row=2, column=1)
        
        # # entry_grp = ttk.Combobox(state="select",
        # #                         values=["Python", "C", "C++", "Java"])(main_frame, width=20, cursor="xterm")
        # # entry_grp.grid(row=3,column=1)
        
        # entry_grp = ttk.Combobox(main_frame, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], width=20, cursor="xterm")
        # entry_grp.grid(row=3,column=1)

        # entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        # entry_pw.grid(row=4, column=1)
        
        # button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        # button.grid(row=5, column=1)

        def signup():
            # Creates a text file with the Username and password
            user = en1.get()
            pw = en6.get()
            rpw = en7.get()
            phone = en4.get()
            bloodGrp = cv.get()
            gender = gen.get()
            validation = validate_user(phone)
            print(user+" "+pw+" "+phone+" "+bloodGrp)
            if validation and pw==rpw:
                tk.messagebox.showerror("Information", "That Username already exists")
            else:
                if len(pw) > 3:
                    # credentials = open("credentials.txt", "a")
                    # credentials.write(f"Username,{user},Password,{pw},\n")
                    # credentials.close()
                    
                    query = "insert into patients(PName, PPhone, Gender, PBlood, Password) values('"+user+"','"+phone+"','"+gender+"','"+bloodGrp+"','"+pw+"')"
                    print(query)
                    db_conn.mycursor.execute(query)
                    tk.messagebox.showinfo("Information", "Your account details have been stored.")
                    SignupPage.destroy(self)

                else:
                    tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")

        def validate_user(phone):
            # Checks the text file for a username/password combination.
            try:
                query = "Select * from patients where PPhone='"+phone+"'"
                
                print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchall()
                if(len(row)==1):
                    return True
                return False
                
            except ConnectionError:
                print("User already exists")
                return False



# root = SignupPage()
# root.title("Sign Up Page")
# root.mainloop()