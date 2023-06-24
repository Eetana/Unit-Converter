'km','m','mm','inch','ft''yd','mi','NM'
# m to km
def m_to_km(m:float):
    km = m / 1000
    return km

# km to m
def km_to_m(km:float):
    m = km * 1000
    return m

# m to mm
def m_to_mm(m:float):
    mm = m * 1000
    return mm

# mm to m
def mm_to_m(mm:float):
    m = mm / 1000
    return m


# inch to mm
def inch_to_mm(inch:float):
    mm = inch * 25.4
    return mm

# mm to inch
def mm_to_inch(mm:float):
    inch = mm / 25.4
    return inch
