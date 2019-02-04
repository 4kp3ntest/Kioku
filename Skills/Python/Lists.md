[2, 1, 4, 2].count(2)
>>> 2
[2, 1, 4, 2].index(1)
>>> 1

# Copy a list
new_list = l.copy()

# Sort a list
sorted(list)
#### prefer lower case words 
sorted(list, key=str.lower)
sorted(list, key=reverse)



# Remove duplicates with 'set'
set(list|str)
#### or to keep order
from collections import OrderedDict
"".join(OrderedDict.fromkeys(foo))

# Make a dict from this set with all values 0
d = dict.fromkeys(set, 0)
