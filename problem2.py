#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""
import math

def hypotenuse(a,b,c):
    if c == False:
        d = a**2 + b**2
        d = math.sqrt(d)
        return d
    elif c == True:
        if a > b:
            d = a**2 - b**2
            d = math.sqrt(d)
            return d
        elif b > a:
            d = b**2 - a**2
            d = math.sqrt(d)
            return d

x = hypotenuse(5,3,True)
print(x)