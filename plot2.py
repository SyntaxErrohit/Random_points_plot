import matplotlib.pyplot as plt
import random
import math

size = 10000

pts = []

highest_pow = random.randint(10, 20)
eqn = ""

for i in range(highest_pow, -1, -1):
    eqn += f"{random.randint(50, 120)}*math.tan(x)**{i}+"

eqn = eqn[:-1]

for i in range(-size,size+1):
    y = eval(eqn.replace("x",f"{i}"))
    pts.append(y)

print(eqn)
plt.plot(pts)
plt.show()