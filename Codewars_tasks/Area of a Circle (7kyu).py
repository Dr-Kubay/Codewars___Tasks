# Complete the function which will return the area of a circle with the given radius.

import math

def circle_area(r):
    if r > 0:
        return (math.pi * (r ** 2))
    raise ValueError

# tests:
print(circle_area(-1))
print(circle_area(0))
print(circle_area(43.26))
print(circle_area(5))
print(circle_area(77.77))