import matplotlib.pyplot as plt
import random

size = 100000
pts = []
xmin, ymin = 100, 100

while len(pts) != size:
    x = random.randint(1, size)
    y = random.randint(1, size)
    if (x,y) not in pts:
        pts.append((x, y))
        if x**2 + y**2 < xmin**2 + ymin**2:
            xmin, ymin = x, y

xpoints = [xmin]
ypoints = [ymin]
newpoints = [(xmin, ymin)]

while len(newpoints) != size:
    d = 1000
    for xnew, ynew in pts:
        if (xnew, ynew) not in newpoints:
            nxy, nyx = newpoints[-1]
            if (xnew-nxy)**2 + (ynew-nyx)**2 < d:
                d = (xnew-nxy)**2 + (ynew-nyx)**2
                x, y = xnew, ynew
    newpoints.append((x,y))
    xpoints.append(x)
    ypoints.append(y)

plt.plot(xpoints, ypoints)
plt.show()
