import math
import scipy.stats as stats

def C(n, r):
    denominator = math.factorial(r) * math.factorial(n-r)
    return math.factorial(n) / denominator

def FindReject(n, p, alpha):
    for i in range(n+1):
        P = stats.binom.cdf(i, n, p)
        if P == alpha:
            return i
        elif P > alpha:
            return i-1

def LowerReject(n, p, significance):
    alpha = significance / 2
    return FindReject(n, p, alpha)

def HigherReject(n, p, significance):
    alpha = 1 - (significance / 2)
    return FindReject(n, p, alpha)+1