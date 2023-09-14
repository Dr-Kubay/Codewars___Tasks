# n this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

def high_and_low(numbers):
    num_list = [int(el) for el in numbers.split()]
    return " ".join([str(max(num_list)), str(min(num_list))])

# tests:
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low("11 22 5 9 1 122"))
print(high_and_low("83 -5 42 -100 -9 4 7 4 -4  8"))