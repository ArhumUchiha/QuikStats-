import math

def C(n, r):
    denominator = math.factorial(r) * math.factorial(n-r)
    return math.factorial(n) / denominator