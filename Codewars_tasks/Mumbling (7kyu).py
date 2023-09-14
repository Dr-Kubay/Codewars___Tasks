# This time no story, no theory. The examples below show you how to write function accum:
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def accum(s):
    index = 1
    result = []
    for letter in s:
        letter = letter * index
        index += 1
        result.append(letter.capitalize())
    return "-".join(result)


# tests:
print(accum("RqaEzty"))
print(accum("ZpglnRxqenU"))
print(accum("accum"))
print(accum("Stanislav"))
print(accum("HbideVbxncC"))