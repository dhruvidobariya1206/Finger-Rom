import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
import Dashboard

class SignupPage(tk.Tk):

    def __init__(self, username, phone, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#8D99AE", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("450x300")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#8D99AE",
                       "foreground": "#8D99AE"}

        # print()
        # print()
        # print()
        # print(username+"       "+phone)
        # print()
        # print()
        # print()

        # lb1= Label(main_frame, text="Enter Name", width=15, font=("arial",12))  
        # lb1.place(x=20, y=120)  
        # en1= Entry(main_frame)  
        # en1.place(x=200, y=120)  
        
        # lb3= Label(main_frame, text="Enter Email", width=15, font=("arial",12))  
        # lb3.place(x=20, y=160)  
        # en3= Entry(main_frame)  
        # en3.place(x=200, y=160)  
        
        # lb4= Label(main_frame, text="Contact Number", width=15,font=("arial",12))  
        # lb4.place(x=20, y=160)  
        # en4= Entry(main_frame)  
        # en4.place(x=200, y=160)
        gen = IntVar()  
        
        lb5= Label(main_frame, text="Select Gender", width=15, font=("arial",12))  
        lb5.place(x=20, y=60)  
         
        # Radiobutton(main_frame, text="Male", padx=5,variable=gen, value=1).place(x=200, y=200)  
        # Radiobutton(main_frame, text="Female", padx =10,variable=gen, value=2).place(x=280,y=200)  
        # Radiobutton(main_frame, text="others", padx=15, variable=vars, value=3).place(x=310,y=240)
        gumb1=Radiobutton(main_frame,text="Male",value = 1,variable = gen).place(x=240, y=60)
        gumb2=Radiobutton(main_frame,text="Female",value = 2,variable = gen).place(x=320,y=60)
        
        lb2= Label(main_frame, text="Age", width=15,font=("arial",12))  
        lb2.place(x=20,y=100)
        en2= Entry(main_frame)  
        en2.place(x=240, y=100)
        
        
        # lb6= Label(main_frame, text="Enter Password", width=15,font=("arial",12))  
        # lb6.place(x=20, y=280)  
        # en6= Entry(main_frame, show='*')  
        # en6.place(x=200, y=280)  
        
        # lb7= Label(main_frame, text="Re-Enter Password", width=15,font=("arial",12))  
        # lb7.place(x=22, y=320)  
        # en7 =Entry(main_frame, show='*')  
        # en7.place(x=200, y=320)  
        
        Button(main_frame, text="Register", width=15, command=lambda: signup()).place(x=150,y=200) 





        def signup():
            # Creates a text file with the Username and password
            user = username
            # pw = en6.get()
            # rpw = en7.get()
            # phone = en4.get()
            age = str(en2.get())
            
            
            gender = gen.get()
            print(gen.get())
            print("gender"+str(gender))
            pgen='F'
            if(gender==2):
                pgen = 'F'
            elif(gender==1):
                pgen='M'
            
            validation = validate_user(phone)
            # print(user+" "+pw+" "+phone+" "+bloodGrp)
            # if pw!=rpw:
            #     tk.messagebox.showerror("Information", "Please enter same password.")
            if(len(phone)!=10):
                tk.messagebox.showerror("Information", "Your phone number needs to be 10 digits long.")
            # elif(len(pw)<3):
            #     tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")
            elif validation:
                tk.messagebox.showerror("Information", "That Username already exists")
            else:
                # if len(pw) > 3:
                    # credentials = open("credentials.txt", "a")
                    # credentials.write(f"Username,{user},Password,{pw},\n")
                    # credentials.close()
                    
                query = "insert into patients(PName, PPhone, Gender, Age) values('"+username+"','"+phone+"','"+pgen+"','"+age+"')"
                print(query)
                db_conn.mycursor.execute(query)
                
                q1=f"SELECT PId from patients WHERE PPhone='{phone}';"
                db_conn.mycursor.execute(q1)
                row1 = db_conn.mycursor.fetchone()
                
                q2 = f"insert into angle_pip(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                db_conn.mycursor.execute(q2)
                q3 = f"insert into angle_tip(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                db_conn.mycursor.execute(q3)
                q4 = f"insert into angle_mcp(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                db_conn.mycursor.execute(q4)
                tk.messagebox.showinfo("Information", "Your account details have been stored.")
                SignupPage.destroy(self)
                Dashboard.Dashboard(username, phone)

                
                
                    

        def validate_user(phone):
            # Checks the text file for a username/password combination.
            try:
                query = "Select * from patients where PPhone='"+phone+"'"
                # print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchall()
                if(len(row)==1):
                    return True
                return False
                
            except ConnectionError:
                print("User already exists")
                return False



# root = SignupPage('tree','9876598630')
# root.title("Sign Up Page")
# root.mainloop()