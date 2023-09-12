# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(list_num):
    for el in list_num:
        if list_num.count(el) % 2 != 0:
            return el


# Tests:
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
print(find_it([10, 10, 0]))