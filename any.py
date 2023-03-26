# # import tkinter as tk
# # import tkinter.simpledialog as sd

# # class CustomDialog(sd.Dialog):
# #     def __init__(self, master, options):
# #         self.options = options
# #         self.result = None
# #         sd.Dialog.__init__(self, master, "Select an option")
        
# #     def body(self, master):
# #         self.var = tk.StringVar()
# #         for option in self.options:
# #             b = tk.Radiobutton(master, text=option, variable=self.var, value=option)
# #             b.pack(anchor='w')
# #         return b

# #     def apply(self):
# #         self.result = self.var.get()
        

# import tkinter as tk
import tkinter.simpledialog as sd

class CustomDialog(sd.Dialog):
    def __init__(self, master, options):
        self.options = options
        self.result = None
        sd.Dialog.__init__(self, master, "Select an option")

    def body(self, master):
        self.var = tk.StringVar()
        self.var.set(self.options[0])
        option_menu = tk.OptionMenu(master, self.var, *self.options)
        option_menu.pack(anchor='w')
        return option_menu

    def apply(self):
        self.result = self.var.get()
        print(self.result + " selected")




