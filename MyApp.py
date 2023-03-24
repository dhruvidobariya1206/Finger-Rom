# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# import db_conn
# import tkinter_demo as tkdemo
# import Login
# import Signup
# import GUI
# import MenuBar


# class MyApp(tk.Tk):

#     def __init__(self, *args, **kwargs):

#         tk.Tk.__init__(self, *args, **kwargs)
#         main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
#         main_frame.pack_propagate(0)
#         main_frame.pack(fill="both", expand="true")
#         main_frame.grid_rowconfigure(0, weight=1)
#         main_frame.grid_columnconfigure(0, weight=1)
#         # self.resizable(0, 0) prevents the app from being resized
#         # self.geometry("1024x600") fixes the applications size
#         self.frames = {}
#         pages = (GUI.Some_Widgets, GUI.PageOne, GUI.PageTwo, GUI.PageThree, GUI.PageFour)
#         for F in pages:
#             frame = F(main_frame, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.show_frame(GUI.Some_Widgets)
#         menubar = MenuBar.MenuBar(self)
#         tk.Tk.config(self, menu=menubar)

#     def show_frame(self, name):
#         frame = self.frames[name]
#         frame.tkraise()

#     def OpenNewWindow(self):
#         tkdemo.OpenNewWindow()

#     def Quit_application(self):
#         self.destroy()
