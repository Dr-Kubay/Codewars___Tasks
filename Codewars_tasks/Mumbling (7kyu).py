# This time no story, no theory. The examples below show you how to write function accum:
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def accum(s):
    result = []
    for count, letter in enumerate(s):
        result.append((letter * (count+1)).capitalize())
    return "-".join(result)


# tests:
print(accum("RqaEzty"))
print(accum("ZpglnRxqenU"))
print(accum("accum"))
print(accum("Stanislav"))
print(accum("HbideVbxncC"))