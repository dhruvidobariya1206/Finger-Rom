from tkinter import *
from tkinter import ttk

import db_conn
# global gender
# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to get the output for selected option
def selection():
    selected = "You selected the option " + str(radio.get())
    label.config(text=selected)
    global gender
    if(radio.get()==1):
        gender='M'
    elif(radio.get()==2):
        gender='F'
    print("gender " + gender)
    # return radio.get()
    # query = f"insert into test values ({radio.get()})"
    # print(query)
    # db_conn.mycursor.execute(query)

radio = IntVar()
Label(text="Your Favourite programming language:", font=('Aerial 11')).pack()

# Define radiobutton for each options
r1 = Radiobutton(win, text="C++", variable=radio, value=1, command=selection)
r1.pack(anchor=N)
r2 = Radiobutton(win, text="Python", variable=radio, value=2, command=selection)
r2.pack(anchor=N)
r3 = Radiobutton(win, text="Java", variable=radio, value=3, command=selection)
r3.pack(anchor=N)

# Define a label widget
selection()
label = Label(win)
label.pack()
print("main " + gender)
win.mainloop()