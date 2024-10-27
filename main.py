import tkinter as tk
from tkinter import ttk
# Define window width and height
width = 300
height = 400

# Start App
app = tk.Tk()

# Apply Width and Height "app.VAR" to the app window-variable
dimensions = f"{width}x{height}"
app.geometry(dimensions)

# Create an abstract grid so we can arrange buttons and labels and stuff
app.grid()



# Instructions label
message = "Type your name:"
instructions = tk.Label(app, text = message)
instructions.grid(column = 0, row = 0)

def replace_text():
    global instructions
    global field

    instructions.destroy
    instructions = tk.Label(app, text = field.get())
    instructions.grid(column=0,row=0)

# Input Field
field = tk.Entry(app)
field.grid(column= 0, row =1)
user_input = field.get()
print(user_input)

# Hello Button
close_button = ttk.Button(app, text="Say Hi", command = replace_text)
close_button.grid(column = 0, row = 3)



# Keep app open until closing
app.mainloop()
