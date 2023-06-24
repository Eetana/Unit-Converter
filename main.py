import tkinter as tk
import screeninfo
from conversion import convert_unit

# Get the primary screen information
screen_info = screeninfo.get_monitors()[0]

# Retrieve the screen dimensions
sw = round(screen_info.width * 0.3)
sh = round(screen_info.height * 0.5)

# List of available units that can be selected
available_units = ['K','C','F','R','L','gal','pt','qt','oz','km','m','mm','inch','ft','yd','mi','NM','kg','t','lb','LT', 'st']

# Initialise variable to store the selected units
initial_unit = ""
desired_unit = ""

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
unit.place(x=sw*0.22, y=sh*0.56)

#Initialize a Label to indicate where to select the new unit
new_unit= tk.Label(canvas, text="New Unit", font=("Courier 12 bold"))
new_unit.place(x=sw*0.138, y=sh*0.62)

#Create an Entry widget to accept User Input
value_entry= tk.Entry(canvas, width= 10)
value_entry.focus_set()
value_entry.place(x=sw*0.32, y=sh*0.5)
   
# Function to trigger when a unit is selected and display it
def change_text(selection):
    string = f'Current unit: {selection}'
    unit_label.configure(text=string)

# Function to determine the original unit
def init_unit(selection):
        
    global initial_unit
    global desired_unit
    global new_menu
    global button
    
    initial_unit = selection
    
    # Reset list of options
    for choice in available_units:
        new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))
        
    if selection in ['K','C','F','R']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['K','C','F','R']:
            if selection == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))
            
        if desired_unit not in ['K','C','F','R']:
            wanted_unit.set("-")
            desired_unit = ""
            button.configure(state=tk.DISABLED)
        
    elif selection in ['L','gal','pt','qt','oz']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['L','gal','pt','qt','oz']:
            if selection == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))
            
        if desired_unit not in ['L','gal','pt','qt','oz']:
            wanted_unit.set("-")
            desired_unit = ""
            button.configure(state=tk.DISABLED)
    
    elif selection in ['km','m','mm','inch','ft','yd','mi','NM']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['km','m','mm','inch','ft','yd','mi','NM']:
            if selection == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))    
            
        if desired_unit not in ['km','m','mm','inch','ft','yd','mi','NM']:
            wanted_unit.set("-")
            desired_unit = ""
            button.configure(state=tk.DISABLED)
            
    elif selection in ['kg','t','lb','LT', 'st']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['kg','t','lb','LT', 'st']:
            if selection == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))    
            
        if desired_unit not in ['kg','t','lb','LT', 'st']:
            wanted_unit.set("-")
            desired_unit = ""
            button.configure(state=tk.DISABLED)
        
    if initial_unit != desired_unit and desired_unit != "": button.configure(state=tk.NORMAL)
    
            
    
# Function that triggers for above
def unit_selection(selection):
    global initial_unit
    global desired_unit
    global button

    desired_unit = selection
    
    if initial_unit != desired_unit and desired_unit != "": button.configure(state=tk.NORMAL)
    

# Create the pull down selection for the initial unit
old_unit = tk.StringVar()
old_unit.set("-")
old_menu = tk.OptionMenu(window, old_unit, *available_units, command=init_unit)
old_menu.place(x=sw*0.32, y=sh*0.548)

# Create the pull down selection for the new unit
wanted_unit = tk.StringVar()
wanted_unit.set("-")
new_menu = tk.OptionMenu(window, wanted_unit, *available_units, command=unit_selection)
new_menu.place(x=sw*0.32, y=sh*0.608)

# Function to trigger when the "Convert" button is clicked so the number is converted as displayed
def display_text():
    
    global value_entry
    
    convereted_number_string = convert_unit(initial_unit, desired_unit)
    # convereted_number_string = str(value_entry.get())
    string = 'Converted Value: ' + convereted_number_string
    value_label.configure(text=string)
    
    global initial_unit
    global desired_unit
    initial_unit = desired_unit 
    desired_unit = ""
    change_text(initial_unit)
    
    old_unit.set(initial_unit)
    wanted_unit.set("-")

    if initial_unit in ['K','C','F','R']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['K','C','F','R']:
            if initial_unit == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))
            
        
    elif initial_unit in ['L','gal','pt','qt','oz']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['L','gal','pt','qt','oz']:
            if initial_unit == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))
    
    elif initial_unit in ['km','m','mm','inch','ft','yd','mi','NM']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['km','m','mm','inch','ft','yd','mi','NM']:
            if initial_unit == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))    
            
    elif initial_unit in ['kg','t','lb','LT', 'st']:
        new_menu['menu'].delete(0, 'end')
        for choice in ['kg','t','lb','LT', 'st']:
            if initial_unit == choice: continue
            new_menu['menu'].add_command(label=choice, command=tk._setit(wanted_unit, choice, unit_selection))    
        
    button.configure(state=tk.DISABLED)

#Create a Button to convert and default to disabled
button = tk.Button(canvas, text= "Convert",width=20,command= display_text)
button.place(x=(sw-20)*0.4, y=sh*0.68)
button.configure(state=tk.DISABLED)

window.mainloop()