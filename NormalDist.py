import scipy.stats as st
import math as m
import pyperclip

def getZ(num, mean, sd):
    diff = (num - mean)
    Zscore = diff/sd
    print(Zscore)

    return Zscore

def PMore(num, mean, sd):
    num = float(num)
    mean = float(mean)
    sd = float(sd)
    Zscore = getZ(num, mean, sd)

    return 1 - st.norm.cdf(Zscore)

def PLess(num, mean, sd):
    answer = 1 - PMore(num, mean, sd)

    print(answer)
    pyperclip.copy(str(answer))
    return answer

def printPMore(num, mean, sd):
    answer = PMore(num, mean, sd)

    print(answer)
    pyperclip.copy(str(answer))
    return answer

def PBetween(num1, num2, mean, sd):
    num1 = float(num1)
    num2 = float(num2)

    if num1 > num2:
        swap = num1
        num1 = num2
        num2 = swap
    
    p1 = PLess(num1, mean, sd)
    p2 = PLess(num2, mean, sd)

    answer = p2 - p1

    print(answer)
    pyperclip.copy(str(answer))
    return answer

def PCLTLess(num, mean, sd, samples):
    num = float(num)
    mean = float(mean)
    sd = float(sd)
    samples = float(samples)

    s_sd = sd / (m.sqrt(samples))

    z = getZ(num, mean, s_sd)

    answer = st.norm.cdf(z)

    return answer

def printPCLTLess(num, mean, sd, samples):
    answer = PCLTLess(num, mean, sd, samples)

    print(answer)
    pyperclip.copy(str(answer))
    return(answer)

def PCLTMore(num, mean, sd, samples):
    answer = 1 - PCLTLess(num, mean, sd, samples)

    print(answer)
    pyperclip.copy(str(answer))
    return answer

def PCLTBetween(num1, num2, mean, sd, samples):
    num1 = float(num1)
    num2 = float(num2)
    
    if num1 > num2:
        swap = num1
        num1 = num2
        num2 = swap

    p1 = PCLTLess(num1, mean, sd, samples)
    p2 = PCLTLess(num2, mean, sd, samples)

    answer = p2 - p1

    print(answer)
    pyperclip.copy(str(answer))
    return answer