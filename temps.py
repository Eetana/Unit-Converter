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