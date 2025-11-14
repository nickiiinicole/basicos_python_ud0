import math

def area_circle(radio):
    if radio <= 0:
        return None
    
    return math.pi * radio**2 

def volume_cilinder(radio, height):
    
    if height <= 0 or radio<=0:
        return None
    
    area_base = area_circle(radio)
    
    return format(area_base * height, ".2f")