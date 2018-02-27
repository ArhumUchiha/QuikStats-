def getK(num, mean, sd):
    diff = (num - mean)
    K = diff/sd

    return abs(K)

def WithinK(K):
    return 1 - (1/(K**2))

def Within(num, mean, sd):
    K = getK(num, mean, sd)
    return WithinK(K)

def PLess(num, mean, sd):
    Pwithin = Within(num, mean, sd)
    if num >= mean:
        return (Pwithin/2) + 0.5
    else:
        return 1 - ((Pwithin/2) + 0.5)

def PMore(num, mean, sd):
    return 1 - PLess(num, mean, sd)

def PBetween(num1, num2, mean, sd):
    if num1 > num2:
        swap = num1
        num1 = num2
        num2 = swap
    P1 = PLess(num1, mean, sd)
    P2 = PLess(num2, mean, sd)
    return P2 - P1