import math
x=int(input("Введіть значення x: "))
f = float(3*math.tan(x))/(math.log(math.cos(x),math.e)+4)+math.fabs(x-pow(x,2))
print(f)