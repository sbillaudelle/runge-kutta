from rk import RK4

R = .1
D = 1
m = 0.1


ydot = lambda t, x, y: -(R*y + D*x) / m
xdot = lambda t, x, y: -(m*ydot(t, x, y) + D*x) / R


lv = RK4(xdot, ydot)
res = lv.solve([0, 1], .01, 2d0)

for i in res:
    print i[0], i[1][0], i[1][1]
