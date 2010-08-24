#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# This example implements a simulation of a damped oscillation.
# See http://en.wikipedia.org/wiki/Oscillation for
# more information on the math behind this simulation.

import pylab
from rk import RK4

# Coefficient of Friction
R = .1

# Spring Constant
D = 1

# Mass
m = 0.1

ydot = lambda t, x, y: -(R*y + D*x) / m
xdot = lambda t, x, y: -(m*ydot(t, x, y) + D*x) / R

lv = RK4(xdot, ydot)
t, y = lv.solve([0, 1], .01, 20)

pylab.plot(t, y[0], t, y[1])
pylab.show()
