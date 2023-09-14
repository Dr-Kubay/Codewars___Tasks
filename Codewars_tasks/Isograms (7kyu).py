# Implement a function that determines whether a string that contains only letters is an isogram.
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(string):
    string = string.lower()
    for el in string:
        if string.count(el) > 1:
            return False
    return True



# tests:
print(is_isogram('Dermatoglyphics'))
print(is_isogram('moose'))
print(is_isogram('Daba'))