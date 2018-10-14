import math


def delta(a, b, c):
    return pow(b, 2) - 4 * a * c


def racine1(d, a, b):
    return (-b - math.sqrt(d)) / 2 * a


def racine2(d, a, b):
    return (-b + math.sqrt(d)) / 2 * a


def racine3(a, b):
    return (-b) / 2 * a


def analyse_the_alchemist(expression):
    l = expression.split()
    # manage X, Y Z
    X = int(l[0])
    Y = int(l[1])
    G = int(l[2])
    # init counter
    c = 0
    # for all number, we need to calc delta
    for y in range(Y):
        d = delta(1, y, y-G)

        if d > 0:
            x1 = racine1(d, 1, y)
            x2 = racine1(d, 1, y)
            # convert to int
            intx1 = float(int(x1))
            intx2 = float(int(x2))
            # test if sqrt is positive and integer
            if x1 < 0 and intx1 - x1 == 0.0 and x2 < 0 and intx2 - x2 == 0.0:
                c += 1
        elif d == 0:
            x3 = racine3(1, y)
            intx3 = float(int(x3))
            # test if sqrt is positive and integer
            if x3 > 0 and intx3 - x3 == 0.0:
                c += 1
    return str(c) + "\n"
