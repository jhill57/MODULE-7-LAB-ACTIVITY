def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = dsquared**0.5
        return result

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(area2(2,2,1,1))

#Use the Math function instead
#import math

#def areaofcircle(r):
#   area = math.pi * (r ** 2)
#    return area

#print(areaofcircle(10))
