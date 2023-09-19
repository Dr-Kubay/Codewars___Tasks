# Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.

# Levenshtein Distance, also known as Edit Distance, is used to calculate the difference between two strings.

# Way1
def levenshtein(a, b):
    x = len(a)
    y = len(b)
    d = [[0] * (y + 1) for el in range(x + 1)]

