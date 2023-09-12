def solution(number):
<<<<<<< HEAD
    num_sum = 0
    for el in range(number):
        if el % 3 == 0 or el % 5 == 0:
            num_sum += el
=======
    new_list = []
    if number <= 0:
        return 0
    for el in range(0, number):
        new_list.append(el)
    num_sum = 0
    for n in new_list:
        if n % 3 == 0 or n % 5 == 0:
            num_sum += n
>>>>>>> origin/main
    return num_sum


# number = int(input('Введите значение: '))
# tests:
print(solution(4))
print(solution(16))
print(solution(5))
print(solution(15))
print(solution(200))
print(solution(250))
print(solution(0))
print(solution(-22))