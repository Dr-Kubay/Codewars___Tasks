# Your task is to write such a run-length encoding. For a given string,
# return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ]/

from collections import OrderedDict
def run_length_encoding(s):
    dict = OrderedDict.fromkeys(s, 0)
    for el in s:
        dict[el] += 1

    result = []

    for key, value in dict.items():
        result = result + [str(value), key]
    return result


# tests:
print(run_length_encoding("hello world!"))