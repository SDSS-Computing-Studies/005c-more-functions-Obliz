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
    if c == True:
        p = (a**2)-(b**2)
        p2 = float(math.sqrt(p))
        return p2
    elif c == False:
        return math.sqrt(a**2 + b**2)

x = hypotenuse(5,3,True)
print(int(x))

y = hypotenuse(12,5,False)
print(int(y))

assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4