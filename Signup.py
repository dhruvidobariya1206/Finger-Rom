import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import db_conn
import tkinter_demo as tkdemo
import Dashboard
import Login

gender = ""

class SignupPage(tk.Tk):

    def __init__(self, Patient_Id, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#1c4966", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("450x400")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#8D99AE",
                       "foreground": "#8D99AE"}
        
        def only_numbers(char):
            return char.isdigit()
        validation_num = main_frame.register(only_numbers)
        
        def only_character(char):
            return not char.isdigit()
        validation_char = main_frame.register(only_character)
        
        lb_fname= Label(main_frame, text="First Name", width=15,font=("arial",12), background="#9EAABF")  
        lb_fname.place(x=20,y=60)
        en_fname= Entry(main_frame, validate="key", validatecommand=(validation_char, '%S'))  
        en_fname.place(x=240, y=60)
        
        lb_mname= Label(main_frame, text="Middle Name", width=15,font=("arial",12), background="#9EAABF")  
        lb_mname.place(x=20,y=100)
        en_mname= Entry(main_frame, validate="key", validatecommand=(validation_char, '%S'))  
        en_mname.place(x=240, y=100)
        
        lb_lname= Label(main_frame, text="Last Name", width=15,font=("arial",12), background="#9EAABF")  
        lb_lname.place(x=20,y=140)
        en_lname= Entry(main_frame, validate="key", validatecommand=(validation_char, '%S'))  
        en_lname.place(x=240, y=140)
        
        lb_phone= Label(main_frame, text="Phone Number", width=20, font=("Verdana",12), background="#9EAABF")  
        lb_phone.place(x=20, y=180)  
        en_phone= Entry(main_frame, validate="key", validatecommand=(validation_num, '%S'))  
        en_phone.place(x=240, y=180) 
        
        # def selection():
        #     print()
        gen = IntVar()  
        # print("init"+str(gen.get()))
        lb5= Label(main_frame, text="Select Gender", width=15, font=("Verdana",12), background="#9EAABF")  
        lb5.place(x=20, y=220)  
        
        radio_m=Radiobutton(main_frame,text="Male",variable = gen, value=1, foreground='#FFFFFF', background="#1c4966", font=("Verdana",12))
        radio_m.place(x=240, y=220)
        radio_f=Radiobutton(main_frame,text="Female", variable = gen, value=2, foreground='#FFFFFF', background="#1c4966", font=("Verdana",12))
        radio_f.place(x=320,y=220)
        
        
        
        lb_age= Label(main_frame, text="Age", width=15,font=("arial",12), background="#9EAABF")  
        lb_age.place(x=20,y=260)
        en_age= Entry(main_frame, validate="key", validatecommand=(validation_num, '%S'))  
        en_age.place(x=240, y=260)
          
        lb_occupation= Label(main_frame, text="Occupation", width=15,font=("arial",12), background="#9EAABF")  
        lb_occupation.place(x=20,y=300)
        en_occupation= Entry(main_frame, validate="key", validatecommand=(validation_char, '%S'))  
        en_occupation.place(x=240, y=300)
        
        Button(main_frame, text="Back", width=15, command=lambda: back(), background="#9EAABF").place(x=100,y=340) 
        Button(main_frame, text="Register", width=15, command=lambda: signup(), background="#9EAABF").place(x=250,y=340) 

        # print(str(gen.get()))

        def back():
            SignupPage.destroy(self)
            Login.LoginPage()
            

        def signup():
            # Creates a text file with the Patient_Id and password
            # P_Id = Patient_Id
            # pw = en6.get()
            # rpw = en7.get()
            # phone = en4.get()
            age = str(en_age.get())
            fname = en_fname.get()
            mname = en_mname.get()
            lname = en_lname.get()
            occupation = en_occupation.get()
            phone = en_phone.get()
            gender = gen.get()
            # print(type(age))
            # print("gender"+str(gender))
            # pgen='F'
            if(gender==2):
                pgen = 'F'
            elif(gender==1):
                pgen='M'
            
            validation = validate_user()
            # print(user+" "+pw+" "+phone+" "+bloodGrp)
            # if pw!=rpw:
            #     tk.messagebox.showerror("Information", "Please enter same password.")
            if(len(phone)!=10):
                tk.messagebox.showerror("Information", "Your phone number needs to be 10 digits long.")
            # elif(len(pw)<3):
            #     tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")
            elif(len(age)>2):
                tk.messagebox.showerror("Information", "Please enter valid age.")
            elif validation:
                tk.messagebox.showerror("Information", "That Patient_Id already exists")
            else:
                # if len(pw) > 3:
                    # credentials = open("credentials.txt", "a")
                    # credentials.write(f"Patient_Id,{user},Password,{pw},\n")
                    # credentials.close()
                    
                query = f"insert into patients(Patient_ID,First_Name,Middle_Name, Last_Name, PPhone, Gender, Age, Occupation) values('{Patient_Id}','{fname}','{mname}','{lname}','{phone}','{pgen}','{age}','{occupation}')"
                # print(query)
                db_conn.mycursor.execute(query)
                
                # q1=f"SELECT PId from patients WHERE PPhone='{phone}';"
                # db_conn.mycursor.execute(q1)
                # row1 = db_conn.mycursor.fetchone()
                
                # q2 = f"insert into angle_pip(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                # db_conn.mycursor.execute(q2)
                # q3 = f"insert into angle_tip(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                # db_conn.mycursor.execute(q3)
                # q4 = f"insert into angle_mcp(P_id,ind,mid,ring,little,thumb) values('{row1[0]}','0','0','0','0','0')"
                # db_conn.mycursor.execute(q4)
                tk.messagebox.showinfo("Information", "Your account details have been stored.")
                SignupPage.destroy(self)
                Dashboard.Dashboard(Patient_Id)

                
                
                    

        def validate_user():
            # Checks the text file for a Patient_Id/password combination.
            try:
                query = f"Select * from patients where Patient_Id='{Patient_Id}'"
                # print(query)
                db_conn.mycursor.execute(query)
                row = db_conn.mycursor.fetchall()
                if(len(row)==1):
                    return True
                return False
                
            except ConnectionError:
                # print("User already exists")
                return False



# root = SignupPage('tree','9876598630')
# root.title("Sign Up Page")
# root.mainloop()