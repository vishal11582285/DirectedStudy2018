#!/usr/bin/env python

####################################################################
###    This is the PYTHON version of program 2.1 from page 19 of   #
### "Modeling Infectious Disease in humans and animals"            #
### by Keeling & Rohani.					    #
###								    #
### It is the simple SIR epidemic without births or deaths.        #
####################################################################

##########################################################################
### Copyright (C) <2008> Ilias Soumpasis                                 #
### ilias.soumpasis@deductivethinking.com                                #
### ilias.soumpasis@gmail.com	                                         #
###                                                                      #
### This program is free software: you can redistribute it and/or modify #
### it under the terms of the GNU General Public License as published by #
### the Free Software Foundation, version 3.                             #
###                                                                      #
### This program is distributed in the hope that it will be useful,      #
### but WITHOUT ANY WARRANTY; without even the implied warranty of       #
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
### GNU General Public License for more details.                         #
###                                                                      #
### You should find a copy of the GNU General Public License at          #
###the Copyrights section or, see http://www.gnu.org/licenses.           #
##########################################################################


import scipy.integrate as spi
import numpy as np
import pylab as pl

beta=1.4247
gamma=0.14286
TS=1.0
ND=70.0
S0=1-1e-6
I0=1e-6
INPUT = (S0, I0, 0.0)


def diff_eqs(INP,t):
	'''The main set of equations'''
	Y=np.zeros((3))
	V = INP
	Y[0] = - beta * V[0] * V[1]
	Y[1] = beta * V[0] * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y   # For odeint

t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

print(RES)

#Ploting
pl.subplot(211)
pl.plot(RES[:,0], '-g', label='Susceptibles')
pl.plot(RES[:,2], '-k', label='Recovereds')
pl.legend(loc=0)
pl.title('Program_2_1.py')
pl.xlabel('Time')
pl.ylabel('Susceptibles and Recovereds')
pl.subplot(212)
pl.plot(RES[:,1], '-r', label='Infectious')
pl.xlabel('Time')
pl.ylabel('Infectious')
pl.show()