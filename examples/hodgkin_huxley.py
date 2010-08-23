#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import math
from rk import RK4

C = 1;
V = 0;
n = 0.32;
m = 0.08;
h = 0.6;
I = 20;
gK = 36;
gNa = 120;
gL = 0.3;
EK = -12;
ENa = 120;
EL = 10.6;

alpha_n = lambda V: 0.01 * (10 - V) / (math.exp(1 - 0.1 * V) - 1)
alpha_m = lambda V: 0.1 * (25 - V) / (math.exp(2.5 - 0.1 * V) - 1)
alpha_h = lambda V: 0.07 * math.exp(-V / 20)

beta_n = lambda V: 0.125 * math.exp(-V / 80)
beta_m = lambda V: 4 * math.exp(-V / 18)
beta_h = lambda V: 1 / (math.exp(3 - 0.1 * V) + 1)

vdot = lambda t, v, n, m, h: (I - gK*(n**4)*(v - EK) - gNa*(m**3)*h*(v - ENa) - gL*(v - EL))/C
ndot = lambda t, v, n, m, h: alpha_n(v) * (1 - n) - beta_n(V) * n
mdot = lambda t, v, n, m, h: alpha_m(v) * (1 - m) - beta_m(V) * m
hdot = lambda t, v, n, m, h: alpha_h(v) * (1 - h) - beta_h(V) * h

rk4 = RK4(vdot, ndot, mdot, hdot)
res = rk4.solve([V, n, m, h], .01, 20)

for i in res:
    print i[0], i[1][0], i[1][1], i[1][2], i[1][3]
