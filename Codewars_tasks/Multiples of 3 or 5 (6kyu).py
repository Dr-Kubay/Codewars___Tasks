def solution(number):
    num_sum = 0
    for el in range(number):
        if el % 3 == 0 or el % 5 == 0:
            num_sum += el
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