# Your task is to write such a run-length encoding. For a given string,
# return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ]/

# from collections import OrderedDict
# def run_length_encoding(s):
#     dict = OrderedDict.fromkeys(s, 0)
#     for el in s:
#         dict[el] += 1
#
#     # result = []
#     #
#     # for key, value in dict.items():
#     #     result = result + [[int(value), key]]
#     # return result


def run_length_encoding(s):
    result = []
    i = 0

    while (i <= len(s) - 1):
        count = 1
        ch = s[i]
        j = i
        while (j < len(s) - 1):
            if (s[j] == s[j + 1]):
                count += 1
                j += 1
            else:
                break
        result = result + [[int(count), ch]]
        i = j + 1
    return result



# tests:
print(run_length_encoding("hello world!"))