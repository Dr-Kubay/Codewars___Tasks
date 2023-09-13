# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    num_list = []
    for el in a:
        if el not in b:
            num_list.append(el)
    return num_list

print(array_diff([1,2,3], [1, 2]))


