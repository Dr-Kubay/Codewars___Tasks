# Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.

# Levenshtein Distance, also known as Edit Distance, is used to calculate the difference between two strings.

# Way1
def levenshtein(a, b):
    x = len(a)
    y = len(b)
    d = [[0] * (y + 1) for i in range(x + 1)]

    for i in range(1, x + 1):
        d[i][0] = i

    for j in range(1, y + 1):
        d[0][j] = j

    for j in range(1, y + 1):
        for i in range(1, x + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,
            d[i][j - 1] + 1,
            d[i - 1][j - 1] + cost)

    return d[x][y]

# tests:
print(levenshtein("lewenstein", "levenshtein"))
print(levenshtein("algorithm", "rhythm"))
print(levenshtein("nayvyedosf","sjxen"))
print(levenshtein("jtbd", "bcx"))
print(levenshtein("kitten", "sitting"))