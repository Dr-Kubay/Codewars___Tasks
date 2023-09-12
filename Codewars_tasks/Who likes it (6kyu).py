# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
# ... like this

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {(len(names)) - 2} others like this"


# tests:
print(likes([]))
print(likes(['Anna']))
print(likes(['Anna', 'Ahsoka']))
print(likes(['Anna', 'Ben', 'Mari']))
print(likes(['Anna', 'Ben', 'Mari', 'Yoda']))
print(likes(['Anna', 'Ben', 'Mari', 'Yoda', 'Kirill']))
print(likes(['Anna', 'Ben', 'Mari', 'Yoda', 'Kirill', 'Alex', 'Namanh']))
print(likes(['Anna', 'Ahsoka', 'Ben', 'Mari', 'Stas', 'Yoda', 'Rick', 'Alex', 'Namanh', 'Anakin']))