# Convert Liter to Gallon
def l_to_gal(L:float):
    gal = L / 3.785
    return gal

# Convert gallon to Liter
def gal_to_l(gal:float):
    L = gal * 3.785
    return L

# Convert gallon to pint
def gal_to_pt(gal:float):
    pt = gal * 6.661
    return pt

# Convert gallon to pint
def pt_to_gal(pt:float):
    gal = pt / 6.661
    return gal

# Convert pint to quart
def pt_to_qt(pt:float):
    qt = pt / 1.665
    return qt

# Convert quart to pint
def qt_to_pt(qt:float):
    pt = qt * 1.665
    return pt

# Convert gallon to ounce
def gal_to_oz(gal:float):
    oz = gal * 128
    return oz

# Convert ounce to gallon
def oz_to_gal(oz:float):
    gal = oz / 128
    return gal

# Convert quart to ounce
def qt_to_oz(qt:float):
    oz = qt * 32
    return oz

# Convert ounze to quart
def oz_to_qt(oz:float):
    qt = oz / 32
    return qt

# Convert quart to gallon
def qt_to_oz(qt:float):
    gal = qt * 4
    return gal

# Convert gallon to quart
def gal_to_qt(gal:float):
    qt = gal / 4
    return qt