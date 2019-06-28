#!/usr/bin/env python

import time
import sys

sys.path.append('/root/lucy')
from Lucy import Lucy

lucy = Lucy()
c = lucy.c

c.psend(color=(1, 0, 0, 0))
#i = 0
#while i < 500:
#    n.fill(n.rand_color())
#    time.sleep(2)
#    n.off()
#    time.sleep(.5)
#    i += 1
#
