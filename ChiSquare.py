import scipy.stats as st
import math as m
import pyperclip

def Greater(val, df):
    answer = 1 - st.chi2.cdf(val, df)

    print(answer)
    pyperclip.copy(str(answer))
    return answer

def Less(val, df):
    answer = st.chi2.cdf(val, df)
    
    print(answer)
    pyperclip.copy(str(answer))
    return answer