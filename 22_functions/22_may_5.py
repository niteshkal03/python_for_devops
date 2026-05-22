# 25. Calculate surface area of a cuboid 
# Input: l = 4, b = 3, h = 2 
# Output: Surface Area = ?

def calc(l,b,h):
    surface_area = 2 * ((l*b)+(b*h)+(h*l))
    return surface_area

print(calc(4,3,2))