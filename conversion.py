from temps import *
from volumes import *
from masses import *
from lengths import *

# Convert from the initial unit type to the desired unit type
def convert_unit(initial, desired, value):
    result = 0
    if initial in ['K','C','F','R']:
        result = convert_temps(initial, desired, value)
        
    elif initial in ['L','gal','pt','qt','oz']:
        result = convert_volumes(initial, desired, value)
        
    elif initial in ['km','m','mm','inch','ft','yd','mi','NM']:
        result = convert_lengths(initial, desired, value)
    
    elif initial in ['kg','t','lb','LT', 'st']:
        result = convert_masses(initial, desired, value)
    
    return str(result)