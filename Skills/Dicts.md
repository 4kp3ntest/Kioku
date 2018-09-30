dict = {'key1' : 'value1', 'key2 : 7}

dict.items()
dict.keys()
dict.values()

# Create a dict with specific order
from collections import OrderedDict
"".join(OrderedDict.fromkeys(foo))

# Switch key - value (multiple values get omitted)
#### python 2.7 uses .iteritems()
d_new = dict((y,x) for x,y in d_old.items())


# Get all KEYs that have a VALUE of 8
[k for k,v in t.items() if v == 8]
Out[48]: ['s', 'z', 'r', 'b', 'g', 'k']

