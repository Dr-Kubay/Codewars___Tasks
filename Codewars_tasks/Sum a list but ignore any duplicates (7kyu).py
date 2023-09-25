# Please write a function that sums a list, but ignores any duplicate items in the list.

def sum_no_duplicates(l):
    result = 0
    for el in l:
        if l.count(el) > 1:
            result += 0
        if l.count(el) == 1:
            result += el
    return result




print(sum_no_duplicates([3, 4, 3, 6]))