#!/usr/bin/env python

from Chopper import *
import time

chopper = Chopper()
n = chopper.n1

n.fill(n.red)
time.sleep(5)
n.off()
#i = 0
#while i < 500:
#    n.fill(n.rand_color())
#    time.sleep(2)
#    n.off()
#    time.sleep(.5)
#    i += 1
#
