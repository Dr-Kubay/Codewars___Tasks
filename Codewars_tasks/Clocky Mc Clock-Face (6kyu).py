from math import floor

# First solution:
def what_time_is_it(angle):
    h = floor(angle / 30)
    m = floor(angle % 30)
    if h == 0:
        h = "12"
    elif h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    return f"{h}:{m}"


print(what_time_is_it(17.3))
print(what_time_is_it(303.242))
print(what_time_is_it(193.787))
print(what_time_is_it(180))
print(what_time_is_it(44.6565))
print(what_time_is_it(0))
print(what_time_is_it(360))