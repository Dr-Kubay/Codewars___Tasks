def diving_minigame(lst):
    breath = 10
    for el in lst:
        if el >= 0:
            breath = min(10, breath + 4)
        else:
            breath -= 2
        if breath <= 0:
            return False
    return True

# Tests:
print(diving_minigame([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2]))
print(diving_minigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(diving_minigame([-3, -6, -2, -6, -2]))
print(diving_minigame([-4, -3, -4, -3, 5, 2, -5, -20, -42, -4, 5, 3, 5]))
print(diving_minigame([0, -4, 0, -4, -5, -2]))
print(diving_minigame([1, 2, 1, 2, 1, 2, 1, 2, 1, -3, -4, -5, -3, -4]))
print(diving_minigame([-5, -15, -4, 0, 5]))
print(diving_minigame([20, 3, 4, -20, 14, 3, 8, -18, -20, -13, 13, -14, -12, -1, 20, -6, -20, -2]))
