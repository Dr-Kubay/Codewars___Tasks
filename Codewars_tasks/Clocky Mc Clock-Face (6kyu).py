from math import floor

def what_time_is_it(angle):
    mins = angle * 2
    h = floor(mins / 60)
    m = floor(mins % 60)
    if h == 0:
        h = "12"
    elif h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    return f"{h}:{m}"



print(what_time_is_it(17.3))