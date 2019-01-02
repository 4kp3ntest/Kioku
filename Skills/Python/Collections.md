# Counter
### counts occurences of items in iterable
l = [1, 1, 2, 2, 2, 3]
Counter(l)
>>> {1:2, 2:3, 3:1}

# defaultdict
### has a default value if key is not set
d = defaultdict(list)
d['unknown_key']
>>> []

# OrderedDict
### keeps the order in which items are added
d = OrderedDict()

# deque
### ordered collection with optimized access from its endpoints
queue = deque(['Valfaris', 'Ifrit', 'Ixion', 'Shiva'])
queue.append('Bahamut')
queue.popleft()
queue.pop()
