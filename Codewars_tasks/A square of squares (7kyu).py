# Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer;
# in other words, it is the product of some integer with itself.

import math

def is_square(n):
    if n >= 0:
        if math.sqrt(n) % 1 == 0:
            return True
    return False


# tests:
print(is_square(-1))
print(is_square(0))
print(is_square(25))
print(is_square(8))
print(is_square(625))