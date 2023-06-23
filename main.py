import tkinter as tk
import screeninfo

# Get the primary screen information
screen_info = screeninfo.get_monitors()[0]

# Retrieve the screen dimensions
sw = round(screen_info.width * 0.3)
sh = round(screen_info.height * 0.5)


# SI; meter, kg, liter, kelvin/celcius
# Length: foot, inch, yard, mile, nautical mile 
# Mass: ounce, pound, stone, ton
# Capacity: gallon, pint, quart, fluid ounce
# Temp: Kelvin, Celcius, Fahrenheit, Rankine, Reaumur, Newton, Delisle, Romer, Wedwood

# Convert Fahrenheit to Celcius
def fah_to_cel(fah:float):
    
    # c = (f - 32)* 5/9
    cel = (fah - 32) * (5/9)
    return cel

# Convert Celcius to Fahrenheit
def cel_to_fah(cel:float):
    
    # c = (f - 32)* 5/9
    fah = (9/5 * cel) + 32
    return fah

# Convert Celcius to Kelvin 
def cel_to_kel(cel:float):
    
    # k = c + 273.15
    kel = cel + 273.15
    return kel

# Convert Kelvin to Celcius 
def kel_to_cel(kel:float):
    
    # k = c + 273.15
    cel = kel - 273.15
    return cel

# Kelvin to Rankine
def kel_to_rankine(kel:float):

    ran = kel * (9/5)
    return ran

# Rankine to Kelvin
def kel_to_rankine(ran:float):

    kel = ran * (5/9)
    return ran

# Rankine to fahrenheit
def rankine_to_fah(ran:float):

    fah = ran - 459.67
    return fah

# fahrenheit to Rankine
def fah_to_ran(fah:float):

    ran = fah + 459.67
    return ran

# Create a window
window = tk.Tk()

# Set the window title
window.title("Unit Converter")
dim_string = f'{sw}x{sh}'
window.geometry(dim_string)

# Create a canvas
canvas = tk.Canvas(window, width=sw, height=sh)
canvas.pack()
canvas.place(x=0, y=0)

#Initialize a Label to display the User Input in the desired unit
value_label= tk.Label(canvas, text="Converted Value: -", font=("Courier 16 bold"))
value_label.place(x=sw*0.205, y=sh*0.3)

#Initialize a Label to display the User Input for the desired unit
unit_label= tk.Label(canvas, text="Current unit: -", font=("Courier 16 bold"))
unit_label.place(x=sw*0.29, y=sh*0.2)

#Initialize a Label to indicate value input
value= tk.Label(canvas, text="Value", font=("Courier 12 bold"))
value.place(x=sw*0.2, y=sh*0.5)

#Initialize a Label to indicate unit input
unit= tk.Label(canvas, text="Unit", font=("Courier 12 bold"))
unit.place(x=sw*0.2, y=sh*0.55)

#Create an Entry widget to accept User Input
value_entry= tk.Entry(canvas, width= 10)
value_entry.focus_set()
value_entry.place(x=sw*0.32, y=sh*0.5)

def display_text():
    global value_entry
    string= value_entry.get()
    value_label.configure(text=string)
   
def change_text(selection):
    global value_entry
    string = f'Current unit: {selection}'
    unit_label.configure(text=string)
   
def unit_selection(selection):
    change_text(selection)
    print(selection)

#Create a Button to validate Entry Widget
tk.Button(canvas, text= "Convert to",width=20,command= display_text).place(x=(sw-20)*0.4, y=sh*0.6)

options = tk.StringVar()
options.set("What is the input unit?")
menu = tk.OptionMenu(window, options, 'a', 'b', 'c', command=unit_selection)
menu.place(x=sw*0.2, y=sh*0.6)

window.mainloop()

