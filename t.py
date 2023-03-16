import tkinter as tk

root = tk.Tk()

# Create a list of options for the dropdown input
options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Create a StringVar object to store the selected option
selected_option = tk.StringVar()

# Set the default value of the StringVar object to the first option
selected_option.set(options[0])

# Define a function to update the selected option in the StringVar object
def update_selected_option(*args):
    selected_option.set(dropdown.get())

# Create the dropdown input widget
dropdown = tk.OptionMenu(root, selected_option, *options)

# Add the dropdown input widget to the GUI
dropdown.pack()

# Call the update_selected_option function when an option is selected
selected_option.trace("w", update_selected_option)

# Run the main event loop
root.mainloop()
