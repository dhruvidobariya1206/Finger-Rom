from tkinter import Tk, StringVar, ttk

class msgBox:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("250x100")
        self.parent.resizable(0, 0)
        self.box_value = None
        
    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value, state='readonly')
        self.box['values'] = ('Left', 'Right')
        self.box.current(0)
        self.box.place(x=30,y=10)
    
        ok_button = ttk.Button(self.parent, text="OK", command=self.parent.destroy)
        ok_button.place(x=20,y=50)
        
        cancel_button = ttk.Button(self.parent, text="Cancel", command=self.parent.destroy)
        cancel_button.place(x=140,y=50)
        
    def show(self):
        self.combo()
        self.parent.wait_window(self.parent)
        return self.box_value.get()
