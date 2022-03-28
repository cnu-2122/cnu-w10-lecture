import matplotlib.pyplot as plt
import numpy as np

def P(x, n):
    '''
    Returns the nth Legendre polynomial
    evaluated at x.
    '''
    if n == 0:
        return 1 * np.ones_like(x)
    
    elif n == 1:
        return x
    
    else:
        P_n_minus_2 = 1
        P_n_minus_1 = x
        for i in range(2, n+1):
            P_n = ((2*i - 1) * x * P_n_minus_1 - (i - 1) * P_n_minus_2) / i
            
            P_n_minus_2 = P_n_minus_1
            P_n_minus_1 = P_n
            
        return P_n
