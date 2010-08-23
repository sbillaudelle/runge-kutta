import math
from rk import RK4

rk4 = RK4(lambda t, y, z: math.cos(t), lambda t, y, z: -y)
res = rk4.solve([0, 1], .01, 2*math.pi)

for i in res:
    print i[0], i[1][0], i[1][1]
