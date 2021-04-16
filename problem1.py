#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

def convertTemp(a,b):
    if b == 'C':
        x = (a * 1.8) + 32
        return x
    elif b == 'F':
        x = (a - 32) / 1.8
        return x
