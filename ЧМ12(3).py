import numpy as np 
import matplotlib.pyplot as plt  

def f(x, y): 
    return x + np.sin(y/3)

a = 1.6 # ліва межа відрізку 
b = 2.6 # права межа відрізку 
h = 0.1 # крок 
y0 = 4.6 # початкова умова
n = int((b - a) / h) # кількість кроків 

x = np.linspace(a, b, n+1) # задаємо x 
y = np.zeros(n+1)
y[0] = y0 

for i in range(n): 
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i])+h*f(x[i],y[i]))*h/2

print("x =", x, "\ny =", y)

plt.plot(x, y, "o-")
plt.xlabel("x")  
plt.ylabel("y")  
plt.title("Метод Ейлера-Коші")  
plt.grid()  
plt.show()




