#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# This example implements the Lotka-Volterra equation.
# See http://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation for
# more information.

import pylab
from rk import RK4

# Nope. We don't explain the parameters. RTFM.
A1 = .1
A2 = .05
B1 = .01
B2 = 0.001

xdot = lambda t, x, y: A1*x - x*y*B1
ydot = lambda t, x, y: B2*x*y - A2*y

lv = RK4(xdot, ydot)
t, y = lv.solve([80, 40], .1, 250)

pylab.plot(t, y[0], t, y[1])
pylab.show()
