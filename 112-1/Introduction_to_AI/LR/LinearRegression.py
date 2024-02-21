import matplotlib.pyplot as plt
import numpy as np

def linear_regression(x, y):
    x = np.array(x)
    y = np.array(y)

    n = len(x)
    Sx = sum(x)
    Sy = sum(y)
    Sxx = sum([i**2 for i in x])
    Sxy = sum([i*j for i,j in zip(x,y)])

    a = (Sxy*n - Sy*Sx) / (Sxx*n - Sx*Sx) # 2552.212389380531
    b = (Sxy*Sx - Sy*Sxx) / (Sx*Sx - n*Sxx) # 24396.46017699115
    line = [a*x + b for x in x]
    print(f'f(x): {a}x + {b}')
    return line

# Seniority
x = [1, 2, 3, 3.5, 4, 4.5, 6, 6, 7]
# Salary
y = [30000, 25000, 35000, 32000, 35000, 32000, 35000, 50000, 40000]

line = linear_regression(x, y)

plt.scatter(x, y, label='Data Points')

plt.plot(x, line, color='red', label='Linear Regression Line')

plt.xlabel('Seniority')
plt.ylabel('Salary')
plt.title('Linear Regression')

plt.legend()

plt.show()
