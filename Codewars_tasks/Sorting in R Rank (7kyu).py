import pandas as pd

def rank(lst):
    s = pd.Series(lst).rank()
    return [j-1 for i,j in s.items()]

# tests:
print(rank([1, 3, 3, 9, 8]))
print(rank(["z", "c", "f", "b", "c"]))
print(rank([8, 8, 8, 5, 5, 5, 3, 2]))
print(rank([1, 2, 0, 3, 7, 1, 11, 1, 2]))
print(rank(["d", "f", "g", "a", "d", "a", "d", "y"]))