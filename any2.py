# import tkinter as tk
# import tkinter.simpledialog as sd
# import any



# # Example usage
# # Example usage
# root = tk.Tk()
# root.withdraw() # Hide the main window
# options = ['Option 1', 'Option 2', 'Option 3']
# dialog = any.CustomDialog(root, options)
# dialog.mainloop() # Start the dialog event loop


from tkinter import Tk, StringVar, ttk
class Application:

    def __init__(self, parent):
        self.parent = parent
        self.combo()

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = ('A', 'B', 'C')
        self.box.current(0)
        self.box.grid(column=0, row=0)

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()