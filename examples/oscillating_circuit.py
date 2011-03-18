#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# This example implements a simulation of an oscillation.
# See http://en.wikipedia.org/wiki/Oscillation for
# more information on the math behind this simulation.

import pylab
from rk import RK4

# Inductance
L = 1 * 10**-2

# Capacity
C = 40 * 10**-3

Qdotdot = lambda t, Q, Qdot: -Q/(L*C)
Qdot = lambda t, Q, Qdot: Qdot

lv = RK4(Qdot, Qdotdot)
t, y = lv.solve([100, 0], 1*10**-5, 0.2)

pylab.grid()
pylab.plot(t, y[0])
pylab.show()
