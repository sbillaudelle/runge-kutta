#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# This example implements a simulation of chargin and discharging
# a capacitor (depending on the parameters used).
# For more information, please refer to the following pages:
# http://hyperphysics.phy-astr.gsu.edu/hbase/electric/capchg.html
# http://hyperphysics.phy-astr.gsu.edu/hbase/electric/capdis.html

import pylab
from rk import RK4

# Resistance of the circuit
R = 1 * 10**3

# Capacity of the capacitor
C = 40 * 10**-3

# Charge at the beginning of the simulation
C0 = 0

# Voltage
U0 = 5 * 10**3

Qdot = lambda t, Q: U0/R - Q/(R*C)

lv = RK4(Qdot)
t, y = lv.solve([C0], .1, 500)

pylab.plot(t, y[0])
pylab.show()
