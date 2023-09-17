# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = list(text.lower())
    count = {el: text.count(el) for el in set(text)}
    count = sorted(count.values())
    result = 0
    for i in count:
        if i > 1:
            result += 1
    return result


print(duplicate_count("abcde"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
