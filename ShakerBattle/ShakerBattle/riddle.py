def digitCounterWith0(number):
    # return the transform number
    # create accumulator
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    height = 0
    nine = 0
    # acc in the number
    for i in number:
        if i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        elif i == 6:
            six += 1
        elif i == 7:
            seven += 1
        elif i == 8:
            height += 1
        elif i == 0:
            zero += 1
        else:
            nine += 1
    n = []
    if zero > 0:
        n.append(zero)
        n.append(0)
    if one > 0:
        n.append(one)
        n.append(1)
    if two > 0:
        n.append(two)
        n.append(2)
    if three > 0:
        n.append(three)
        n.append(3)
    if four > 0:
        n.append(four)
        n.append(4)
    if five > 0:
        n.append(five)
        n.append(5)
    if six > 0:
        n.append(six)
        n.append(6)
    if seven > 0:
        n.append(seven)
        n.append(7)
    if height > 0:
        n.append(height)
        n.append(8)
    if nine > 0:
        n.append(nine)
        n.append(9)
    return n


def digitCounterWithout0(number):
    # return the transform number
    # create accumulator
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    height = 0
    nine = 0
    # acc in the number
    for i in number:
        if i == 1:
            one += 1
        elif i == 2:
            two += 1
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        elif i == 6:
            six += 1
        elif i == 7:
            seven += 1
        elif i == 8:
            height += 1
        else:
            nine += 1
    n = []
    if one > 0:
        n.append(one)
        n.append(1)
    if two > 0:
        n.append(two)
        n.append(2)
    if three > 0:
        n.append(three)
        n.append(3)
    if four > 0:
        n.append(four)
        n.append(4)
    if five > 0:
        n.append(five)
        n.append(5)
    if six > 0:
        n.append(six)
        n.append(6)
    if seven > 0:
        n.append(seven)
        n.append(7)
    if height > 0:
        n.append(height)
        n.append(8)
    if nine > 0:
        n.append(nine)
        n.append(9)
    return n


# from python 2
def cmp(a, b):
    return (a > b) - (a < b)


def analyse_riddle(expression1, expression2):
    # keep the list in a variable
    l = [int(i) for i in expression1[:-1]]
    old1 = l
    old2 = []
    old3 = []
    if 0 in l:
        for i in range(0, int(expression2)):
            # process digitCounter
            l = digitCounterWith0(l)
            # verify if it is the same result before continue process
            # case res is the same pattern
            if cmp(old1, l) == 0:
                return ''.join(str(x) for x in old1) + "\n"
            # case res crossed + 1, we have 2 pattern
            if cmp(old2, l) == 0:
                # detect which pattern need to be use
                remainder = int(expression2) - i
                # if even take n-1 else take n
                if remainder % 2 == 0:
                    return ''.join(str(x) for x in old1) + "\n"
                else:
                    return ''.join(str(x) for x in old2) + "\n"
            # case res crossed + 1, we have 3 pattern
            if cmp(old3, l) == 0:
                # detect which pattern need to be use
                remainder = int(expression2) - i
                # if even take n-1 else take n
                if remainder % 3 == 0:
                    return ''.join(str(x) for x in old2) + "\n"
                elif remainder % 2 == 0:
                    return ''.join(str(x) for x in l) + "\n"
                else:
                    return ''.join(str(x) for x in old1) + "\n"
            # keep the list in a variable
            old3 = old2
            old2 = old1
            old1 = l

    else:
        for i in range(0, int(expression2)):
            # process digitCounter
            l = digitCounterWithout0(l)
            # verify if it is the same result before continue process
            # case res is the same pattern
            if cmp(old1, l) == 0:
                return ''.join(str(x) for x in old1) + "\n"
            # case res crossed + 1, we have 2 pattern
            if cmp(old2, l) == 0:
                # detect which pattern need to be use
                remainder = int(expression2) - i
                # if even take n-1 else take n
                if remainder % 2 == 0:
                    return ''.join(str(x) for x in old1) + "\n"
                else:
                    return ''.join(str(x) for x in old2) + "\n"
            # case res crossed + 1, we have 3 pattern
            if cmp(old3, l) == 0:
                # detect which pattern need to be use
                remainder = int(expression2) - i
                # if even take n-1 else take n
                if remainder % 3 == 0:
                    return ''.join(str(x) for x in old2) + "\n"
                elif remainder % 2 == 0:
                    return ''.join(str(x) for x in l) + "\n"
                else:
                    return ''.join(str(x) for x in old1) + "\n"
            # keep the list in a variable
            old3 = old2
            old2 = old1
            old1 = l
    return ''.join(str(x) for x in l) + "\n"
