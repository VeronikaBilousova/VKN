# Наближення прямою
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def func(x):
    return np.cos(4*x) - x + 1

x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([func(xi) for xi in x])
print('x=', x)
print('y=', y)

def fun(a, x, y):
    return a[0] + a[1] * x - y

a0 = np.array([1, 1])
res_lsq = least_squares(fun, x0=a0, args=(x, y))

print("a0 = %.2f, a1 = %.2f" % tuple(res_lsq.x))

f = lambda x: res_lsq.x[0] + res_lsq.x[1] * x
x_p = np.linspace(min(x), max(x), 20)
y_p = f(x_p)
plt.xlabel('x') 
plt.ylabel('y') 
plt.plot(x, y, 'o')
plt.plot(x_p, y_p, 'b')
plt.title("МНК_наближення прямою")
plt.grid(True)
plt.show()