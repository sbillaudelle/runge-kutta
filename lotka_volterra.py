from rk import RK4

A1 = .1
A2 = .05
B1 = .01
B2 = 0.001

lv = RK4(lambda t, x, y: A1*x - x*y*B1, lambda t, x, y: B2*x*y - A2*y)
res = lv.solve([80, 40], .1, 250)

for i in res:
    print i[0], i[1][0], i[1][1]
