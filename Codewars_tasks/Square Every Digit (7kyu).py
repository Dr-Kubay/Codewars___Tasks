# In this kata, you are asked to square every digit of a number and concatenate them.

def square_digits(num):
    new_num = ''
    for el in str(num):
        new_num += str((int(el))**2)
    return int(new_num)

# Tests:
print(square_digits(9119))
print(square_digits(0))
print(square_digits(255))