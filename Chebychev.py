def getK(num, mean, sd):
    diff = (num - mean)
    K = diff/sd

    return K

def LowerBound(num, mean, sd):
    K = getK(num, mean, sd)
    return 1 - (1/(K**2))