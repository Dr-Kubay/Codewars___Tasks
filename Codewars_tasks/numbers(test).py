def plusOne(n):
    list_num = ""
    for i in n:
        list_num += str(i)
    num = int(list_num)
    num += 1
    str_list = list(str(num))
    for i, v in enumerate(str_list):
        str_list[i] = int(v)
    return str_list

print(plusOne([4, 3, 2, 1]))