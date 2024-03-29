# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    odd_number = [x for x in integers if x % 2 != 0]
    even_number = [x for x in integers if x % 2 == 0]
    return odd_number[0] if len(odd_number) < len(even_number) else even_number[0]



# tests:
print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))