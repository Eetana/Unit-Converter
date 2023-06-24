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

# yard to inch
def yd_to_inch(yd:float):
    inch = yd * 36
    return inch
    
# inch to yard
def inch_to_yd(inch:float):
    yd = inch / 36
    return yd

# foot to inch
def ft_to_inch(ft:float):
    inch = ft * 12
    return inch
    
# inch to foot
def inch_to_ft(inch:float):
    ft = inch / 12
    return ft

# mile to yard
def mi_to_yd(mi:float):
    yd = mi * 1760
    return yd

# yard to mile
def yd_to_mi(yd:float):
    mi = yd / 1760
    return mi
    
# mile_to_km
def mi_to_km(mi:float):
    km = mi * 1.60934
    return km

# km_to_mile
def km_to_mi(km:float):
    mi = km / 1.60934
    return mi

# mile to nautical mile
def mi_to_nm(mi:float):
    nm = mi / 1.15078
    return nm

# nautcial mile to mile
def nm_to_mi(nm:float):
    mi = nm * 1.15078
    return mi