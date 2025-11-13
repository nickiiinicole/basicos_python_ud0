import math

def area_circle(radio):
    if radio <= 0:
        return None
    return format(math.pi * radio**2,".2f")

def volume_cilinder(radio, height):
    
    if height <= 0 or radio<=0:
        return None

    return format(area_circle(radio) * height,".2f")