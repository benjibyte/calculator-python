import os
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkthemes import ThemedTk
import tkinter.font as tkf
# I use an icon by...
#<a href="https://www.freepik.com/icon/calculator_4263413#fromView=keyword&page=1&position=33&uuid=7f8efb46-8b2b-463a-8788-9778055fb08f">Icon by Freepik</a>


# Define window width and height, setup the number string, setuip the ready_to_operate variable that switches from input mode to calculation mode
width = 300
height = 400
num_string_list = []
first_num_digits = True
second_num_digits = False
ready_to_operate = False
global_operator = "" 



# Start App, initialize the font
app = ThemedTk(theme="black")
main_font = tkf.Font(app, family = "Helvetica", size=18, weight = "bold")
first_num_digits = True
# Apply Width and Height "app.VAR" to the app window-variable
dimensions = f"{width}x{height}"
app.geometry(dimensions)
app.title("Calculator")
# Create an abstract grid so we can arrange buttons and labels and stuff
app.grid()
app.resizable(False, False)

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "icon.png")

# Set the window icon
try:
    icon = tk.PhotoImage(file=icon_path)
    app.iconphoto(False, icon)
except tk.TclError as e:
    print(f"Error loading icon: {e}")


for btn in range(10):  # Adjust as needed
    app.grid_rowconfigure(btn, weight=1)  # Make each row expandable
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)

def reset():
    global num_string_list, first_num_digits, ready_to_operate, global_operator, second_num_digits
    num_string_list = [] # Reset it back to an empty list
    first_num_digits = True
    second_num_digits = False
    ready_to_operate = False
    global_operator = ""
    display.config(text = "Cleared Everything")
    
def append_num(num, list_num, old_length=0):
    global ready_to_operate, first_num_digits, second_num_digits
    
    if first_num_digits and second_num_digits == False:
        if len(list_num) == old_length:
            list_num.append(str(num))
        else:
            list_num[old_length] += str(num)
        display.config(text = list_num[old_length])
    elif second_num_digits and first_num_digits == False:
        if len(list_num) == (old_length + 1):
            list_num.append(str(num))
        else:
            list_num[(old_length + 1)] += str(num)
        display.config(text = list_num[(old_length + 1)])
    print(list_num)
    return list_num

def begin_math(operator):
    global ready_to_operate, first_num_digits, global_operator, second_num_digits
    ready_to_operate = True
    first_num_digits = False
    global_operator = operator
    second_num_digits = True
    print(f"preparing to: '{operator}'")
    display.configure(text=str(operator))
    
def do_operation(first_num, second_num, operator):
    global ready_to_operate
    print(f"Ready To Operate : {ready_to_operate}")
    if ready_to_operate:

        if operator == "+":
            result = first_num + second_num
            return result
            # Returns a result to a label to get displayed, I also NEED to call a function that puts this result to the first index of a list
            # call it on line 45 (here) just before the return part
        elif operator == "-":
            result = first_num - second_num
            return result
        elif operator == "x":
            result = first_num * second_num
            return result
        elif operator == "÷":
            
            result = first_num / second_num if first_num != 0 else "You can't divide by 0!"
            return result
        else:
            print("ERROR: Operator symbol invalid!")
            return 0
    else:
        print("ERROR: ready_to_operate is False")

def get_result(): # capable of integer arithmetic, need to make a parser that can tell if there needs any float number, or if there is just zeros after the period.
    global num_string_list, first_num_digits, ready_to_operate, second_num_digits
    first_num = int(num_string_list[0])
    second_num = int(num_string_list[1])

    result = do_operation(first_num, second_num, global_operator)
    # Turns out that you can get 2.5 or float numbers as a result but can't use them in the initial equation!
    num_string_list = [] # Reset it back to an empty list
    first_num_digits = True
    second_num_digits = False
    ready_to_operate = False
    num_string_list = [str(result)]
    
    display.config(text = str(result))
style = Style('darkly')
app_background = "#2C2C2C"

btnstyle = {'width': 12, 'bootstyle': 'dark'}


white_text = "#FFFFFF"
display = ttk.Label(app, font=main_font, anchor='center')
display.grid(row = 1, column= 0, columnspan=5, rowspan = 4, sticky = "nsew", pady=20)
app.configure(bg=app_background)
# Number Buttons LAMBDA
one = ttk.Button(app, text = "1",**btnstyle, padding = 10, command = lambda: append_num(1, num_string_list))
two = ttk.Button(app, text = "2",**btnstyle, padding = 10, command = lambda: append_num(2, num_string_list))
three = ttk.Button(app, text = "3",**btnstyle, padding = 10, command = lambda: append_num(3, num_string_list))
four = ttk.Button(app, text = "4",**btnstyle, padding = 10, command = lambda: append_num(4, num_string_list))
five = ttk.Button(app, text = "5",**btnstyle, padding = 10, command = lambda: append_num(5, num_string_list))
six = ttk.Button(app, text = "6",**btnstyle, padding = 10, command = lambda: append_num(6, num_string_list))
seven = ttk.Button(app, text = "7",**btnstyle, padding = 10, command = lambda: append_num(7, num_string_list))
eight = ttk.Button(app, text = "8",**btnstyle, padding = 10, command = lambda: append_num(8, num_string_list))
nine = ttk.Button(app, text = "9",**btnstyle, padding = 10, command = lambda: append_num(9, num_string_list))
zero = ttk.Button(app, text = "0",**btnstyle, padding = 10, command = lambda: append_num(0, num_string_list))

# Format the Number Buttons
one.grid(row = 7, column = 0, padx=5)
two.grid(row = 7, column = 1, padx=5)
three.grid(row = 7, column = 2, padx=5)

four.grid(row = 6, column = 0, padx=5)
five.grid(row = 6, column = 1, padx=5)
six.grid(row = 6, column = 2, padx=5)

seven.grid(row = 5, column = 0, padx=5)
eight.grid(row = 5, column = 1, padx=5)
nine.grid(row = 5, column = 2, padx=5)

zero.grid(row = 8, column = 1, padx=5)

# The Operator Buttons
add = ttk.Button(app, text = "+",**btnstyle, padding = 10, command = lambda: begin_math("+"))
sub = ttk.Button(app, text = "-",**btnstyle, padding = 10, command = lambda: begin_math("-"))
mult = ttk.Button(app, text = "×",**btnstyle, padding = 10, command = lambda: begin_math("x"))
divi = ttk.Button(app, text = "÷",**btnstyle, padding = 10, command = lambda: begin_math("÷"))
equal = ttk.Button(app, text = "=",**btnstyle, padding = 10, command = lambda: get_result())

# Format the Operator Buttons
add.grid(row = 5, column = 4, padx=5)
sub.grid(row = 6, column = 4, padx=5)
mult.grid(row = 7, column = 4, padx=5)
divi.grid(row = 8, column = 4, padx=5)
equal.grid(row = 8, column = 2, padx=5)

# The CE RESET button
reset = ttk.Button(app, text = "CE",**btnstyle, padding= 10, command = reset)
reset.grid(row = 8, column = 0, padx=5)


# Keep app open until closing
app.mainloop()