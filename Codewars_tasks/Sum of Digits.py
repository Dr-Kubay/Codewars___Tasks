# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.

def digital_root(number):
    if number >= 10:
        return digital_root(sum([int(el) for el in str(number)]))
    else:
        return number

# tests:
print(digital_root(188))
print(digital_root(16))
print(digital_root(1222))
print(digital_root(1871))
print(digital_root(2888))
print(digital_root(888))
print(digital_root(111))