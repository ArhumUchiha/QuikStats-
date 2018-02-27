import scipy.stats as st
import math as m 
import pyperclip

def ExpectedValue(n, prob):
    answer = n * prob
    
    print(answer)
    pyperclip.copy(str(answer))
    return (answer)