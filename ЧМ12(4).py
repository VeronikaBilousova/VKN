#Розв’язок диф. Рівняння за допомогою scipy.integrate import odeint 
import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

a = 1.6 # ліва межа відрізку 
b = 2.6 # права межа відрізку 
h = 0.1 # крок 

# function that returns dy/dx 
def model(y,x):  
    return x + np.sin(y/3) 
y0 = 4.6

# x points 
x = np.linspace(a, b, n+1) # задаємо x 
# solve ODE 
y = odeint(model,y0,x) 
print('x=', x) 
print('y=',y) 

plt.plot(x, y, "o-")
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Розв’язання диф. рівняння') 
plt.grid()  
plt.show()



