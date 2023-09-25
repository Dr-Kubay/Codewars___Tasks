# Please write a function that sums a list, but ignores any duplicate items in the list.

# def sum_no_duplicates(l):
#     result = 0
#     for el in l:
#         if l.count(el) > 1:
#             result += 0
#         if l.count(el) == 1:
#             result += el
#     return result

def sum_no_duplicates(l):
    return sum(el for el in l if l.count(el) == 1)

# tests:
print(sum_no_duplicates([3, 4, 3, 6]))
print(sum_no_duplicates([7, 2, 10, 9, 10, 2, 7, 3, 10, 8, 2, 5]))
print(sum_no_duplicates([9, 8, 3, 1, 8, 1, 7]))
print(sum_no_duplicates([7, 1, 8, 8, 5, 5, 1, 4, 0, 1, 10, 1]))
print(sum_no_duplicates([4, 2, 10, 9, 10, 5, 1, 7, 1, 9, 8, 7, 4, 2, 5, 8, 3, 10, 8]))