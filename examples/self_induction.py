#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# This example implements a simulation of self-inducation.
# For more information, please refer to:
# http://www.ndt-ed.org/EducationResources/CommunityCollege/EddyCurrents/Physics/selfinductance.htm

import pylab
from rk import RK4

# Resistance of the circuit (ohm)
R = 50

# Number of turns
n = 1 * 10**3

# Length of the inductor (m)
l = .1

# Vacuum permeability
m0 = 1.257 * 10**-6

# Conductor permeability (
mr = 1

# Area of cross-section of the coil in (m²)
A = 0.001

# Voltage (V)
U0 = 10

# Calculating the Inductance (H)
L = (m0 * mr * A * n**2) / l

Idot = lambda t, I: (U0 - R*I) / L

lv = RK4(Idot)
t, y = lv.solve([0], 1*10**-6, 2*10**-3)

pylab.plot(t, y[0])
pylab.show()
