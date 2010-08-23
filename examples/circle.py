#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import math
from rk import RK4

xdot = lambda t, y, z: math.cos(t)
ydot = lambda t, y, z: -y

rk4 = RK4(xdot, ydot)
res = rk4.solve([0, 1], .01, 2*math.pi)

for i in res:
    print i[0], i[1][0], i[1][1]
