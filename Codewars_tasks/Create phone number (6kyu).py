# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# def create_phone_number(n):
#     return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# tests:
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 2, 5, 8, 9, 6, 9, 9, 9, 0]))
print(create_phone_number([0, 0, 0, 3, 5, 7, 7, 0, 0, 0]))
print(create_phone_number([1, 1, 1, 2, 2, 2, 3, 3, 3, 0]))
print(create_phone_number([9, 5, 8, 9, 5, 4, 3, 2, 1, 0]))