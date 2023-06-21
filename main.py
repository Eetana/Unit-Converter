import tkinter as tk
import screeninfo

# Get the primary screen information
screen_info = screeninfo.get_monitors()[0]

# Retrieve the screen dimensions
sw = round(screen_info.width * 0.3)
sh = round(screen_info.height * 0.5)


# Normal; meter, kg, liter, kelvin/celcius
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
window.title("Canvas Example")
dim_string = f'{sw}x{sh}'

window.geometry(dim_string)

# # Set the desired canvas dimensions
# cw = 0.3 * sw
# ch = 0.3 * sh

# # Calculate the coordinates to center the canvas
# x = canvas_width // 2
# y = canvas_height // 2

# # Create a canvas
# canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
# canvas.pack()
# canvas.place(x=x, y=y)

# canvas.create_rectangle(50, 50, 350, 250, fill="blue")
# canvas.create_text(200, 150, text="Centered Canvas", fill="white", font=("Arial", 16))

window.mainloop()
