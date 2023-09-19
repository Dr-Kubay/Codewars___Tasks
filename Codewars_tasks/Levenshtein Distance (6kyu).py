# Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.

# Levenshtein Distance, also known as Edit Distance, is used to calculate the difference between two strings.

# Way1
def levenshtein(a, b):
    x = len(a)
    y = len(b)
    d = [[0] * (y + 1) for el in range(x + 1)]

    for el in range(1, x + 1):
        d[el][0] = el

    for n in range(1, y + 1):
        d[0][n] = n

    for n in range(1, y + 1):
        for el in range(1, x + 1):
            if x[el - 1] == y[n - 1]:
                cost = 0
            else:
                cost = 1
            d[el][n] = min(d[x - 1][n] + 1,
            d[el][n - 1] + 1,
            d[el - 1][n - 1] + cost)

    return d[x][y]

# tests:
print(levenshtein("lewenstein", "levenshtein"))
print(levenshtein("algorithm", "rhythm"))
print(levenshtein("nayvyedosf","sjxen"))
print(levenshtein("jtbd", "bcx"))
print(levenshtein("kitten", "sitting"))