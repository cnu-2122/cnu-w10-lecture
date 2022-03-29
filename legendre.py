import matplotlib.pyplot as plt
import numpy as np

def P(x, n):
    '''
    Returns the nth Legendre polynomial
    evaluated at x.
    https://mathworld.wolfram.com/LegendrePolynomial.html
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
    
    
def Pp(x, n):
    '''
    Derivative of nth Legendre polynomial.
    '''
    return (-n * x * P(x, n) + n * P(x, n-1)) / (1 - x**2)

# Evaluate the 5th Legendre polynomial at x=2
# print(P(2, 5))

# Plot the first 5 polynomials
xax = np.linspace(-1, 1, 50000)
fig, ax = plt.subplots()

# for i in range(5):
for i in [3]:
    ax.plot(xax, P(xax, i), label=f'P{i}(x)')
    
ax.axhline(0, color='k')
ax.legend()
# plt.show()


def bisection(F, a, b, tol):
    '''
    Finds the root of F in the interval [a, b] using
    the bisection method, to within an error of tol.
    '''
    # Iteration count
    its = 0

    # Midpoint
    c = 0.5 * (a + b)
    
    # Loop until the root is found
    while abs(F(c)) >= tol:
    # while abs(b - a) >= tol:
        # Increment the iteration count
        its += 1

        if F(a) * F(c) <= 0.0:    # F(a) and F(c) have different signs (or one or both is zero) ...
            b = c                 # ... a root is between a and c (or equals a or c)
        else:
            a = c                 # Else, a root is between c and b (or equals b)

        # Find the next midpoint
        c = 0.5 * (a + b)
    
    # Return the root and the number of iterations
    return c, its

def newton(F, Fp, x0, tol):
    '''
    Newton's method.
    '''
    # Iteration count
    its = 0
    
    # Initialise first guesss
    x = x0
    while abs(F(x)) >= tol:
        # Increment count
        its += 1
        
        # Newton update
        x = x - F(x) / Fp(x)
    
    return x, its




# Find the roots using bisection
n = 3
def F(x):
    return P(x, n)

def Fp(x):
    return Pp(x, n)

# F = lambda x: P(x, 3)

# # Find the leftmost root of 3rd Legendre polynomial
# a, b = -0.85, -0.66
tol = 1e-10

# Find the 3 roots of the 3rd Legendre polynomial
intervals = [[-0.85, -0.66],
             [-0.1, 0.1],
             [0.66, 0.85]]

# Initialise an array to store the roots
xk = []

for i in range(3):
    # root = bisection(F, intervals[i][0], intervals[i][1], tol)
    root = newton(F, Fp, intervals[i][0], tol)
    print(root)
    xk.append(root[0])
    
    
    


# Plot the result on the graph
ax.plot(xk, F(np.array(xk)), 'ro', label='Newton roots')
ax.legend()
plt.show()