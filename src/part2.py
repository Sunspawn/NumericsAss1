# single precision epsilon

EPS = 1.0
N = 0

while True:
    EPS = EPS / 2
    A = EPS + 1.0
    if A == 1.0:
        print(EPS)
        break
    N = N + 1
