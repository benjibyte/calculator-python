import tkinter as tk
from tkinter import ttk
# Define window width and height, setup the number string, setuip the ready_to_operate variable that switches from input mode to calculation mode
width = 300
height = 400
num_string_list = []
append_num_list = False
ready_to_operate = False


# Start App
app = tk.Tk()
append_num_list = True
# Apply Width and Height "app.VAR" to the app window-variable
dimensions = f"{width}x{height}"
app.geometry(dimensions)

# Create an abstract grid so we can arrange buttons and labels and stuff
app.grid()




def append_num(num, list_num):
    global ready_to_operate
    global append_num_list
    if append_num_list == True: # Update the list num, so we can operate on the two numbers later
        list_num.append(num)
        append_num_list = False # Set it to false so the next number is just written on
        
        print(list_num)
        return list_num
    else: # append another digit to the first number and then replace the old "num" in the list
        write_to_num = str(list_num[0]) 
        # There will only be 2 things in the list, because once they are 
        # operated on they are put back into the first index[0] of the num list
        write_to_num += str(num)
        list_num[0] = write_to_num
        ready_to_operate = True
        print(list_num)    



def operator (first_num, second_num, operator):
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
        elif operator == "×":
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

# Display Field

dark_field = "#260a2eFF"
dark_background = "#0C0535FF"
dark_text = "#FFFFFFFF"
display = Text(app, dark_field, dark_text, 18, 12)


# Number Buttons LAMBDA
one = ttk.Button(app, text = "1", command = lambda: append_num(1, num_string_list))
two = ttk.Button(app, text = "2", command = lambda: append_num(2, num_string_list))
three = ttk.Button(app, text = "3", command = lambda: append_num(3, num_string_list))
four = ttk.Button(app, text = "4", command = lambda: append_num(4, num_string_list))
five = ttk.Button(app, text = "5", command = lambda: append_num(5, num_string_list))
six = ttk.Button(app, text = "6", command = lambda: append_num(6, num_string_list))
seven = ttk.Button(app, text = "7", command = lambda: append_num(7, num_string_list))
eight = ttk.Button(app, text = "8", command = lambda: append_num(8, num_string_list))
nine = ttk.Button(app, text = "9", command = lambda: append_num(9, num_string_list))
zero = ttk.Button(app, text = "0", command = lambda: append_num(0, num_string_list))

# Format the Number Buttons
one.grid(row = 3, column = 0)
two.grid(row = 3, column = 1)
three.grid(row = 3, column = 2)

four.grid(row = 2, column = 0)
five.grid(row = 2, column = 1)
six.grid(row = 2, column = 2)

seven.grid(row = 1, column = 0)
eight.grid(row = 1, column = 1)
nine.grid(row = 1, column = 2)

zero.grid(row = 4, column = 1)

# The Operator Buttons
add = ttk.Button(app, text = "+")
sub = ttk.Button(app, text = "-")
mult = ttk.Button(app, text = "×")
divi = ttk.Button(app, text = "÷")
equal = ttk.Button(app, text = "=")

# Format the Operator Buttons
add.grid(row = 1, column = 4)
sub.grid(row = 2, column = 4)
mult.grid(row = 3, column = 4)
divi.grid(row = 4, column = 4)
equal.grid(row = 4, column = 2)

# The CE RESET button
reset = ttk.Button(app, text = "CE")
reset.grid(row = 4, column = 0)




# The way i wrote the operator function makes me want to display one number at a time and then when
# the list has two numbers in it and the ready operator variable is true, then if the user preses 
# the operator button then it operates on both numbers and displays the result while storing the result in the first 
# index of the list and deleting the second index of the list, and setting ready to operate to false again until the user 
# either presses another operator button or the (CE) reset button. 

# Operator Buttons
# add = ttk.Button(app, text = "+", command = )
# sub = ttk.Button(app, text = "-", command = )
# mult = ttk.Button(app, text = "×", command = )
# divi = ttk.Button(app, text = "÷", command = )
# equal = ttk.Button(app, text = "=", command = )




# Keep app open until closing
app.mainloop()
