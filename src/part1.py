def absolute(num):
    if num < 0:
        return num * (-1)
    return num


a = 3.0
b = 4.0
c = 1

print(absolute(a * (b / a - c) - c))
