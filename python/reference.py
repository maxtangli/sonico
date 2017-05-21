import collections

# built-in functions
"""
math: abs(), all(), any(), ascii(), chr(), divmod(), hex(), max(), min(), oct(), ord(), pow(), round(), sum()
type: bool(), bin(), complex(), float(), int()
collection type: bytearray(), bytes(), dict(), enumerate(), frozenset(), list(), map(), memoryview(), range(), set(), str(), tuple()
collection operation: filter(), ?iter(), len(), next(), reversed(), slice(), sorted(), zip()
object: callable(), classmethod(), delattr(), getattr(), hasattr(), hash(), id(), isinstance(), issubclass(), object(), property(), repr(), setattr(), staticmethod(), super(), type(), vars()
io: format(), input(), open(), print()
language: compile(), dir(), eval(), exec(), globals(), help(), locals(), __import__()
"""

# built-in constants and types
"""
constants: False, True, None, NotImplemented, Ellipsis, __debug__
true value testing: false = None, False, __bool__(), zero numberic, empty container, __len__(), otherwise true
boolean operators: and, or, not
comparisons: ==, __eq__() default compare object identity; __lt__(); is, is not.
numeric types: int, float, complex. operation: x // y, x ** y, divmod(x, y) etc.
"""

# iter
"""
iterable: An object capable of returning its members one at a time.
iterator: __iter__(), __next__(). convenient impl: generator, yield.
iterable operations:
    map(function, iterable) -> iterator
    filter(function, iterable) -> iterator
    reduce(function, iterable) -> value
"""

# sequence: list, tuple, range
"""
common operations: x in s, x not ins , s+t, s*n, s[i:j:k], len(s), min(s), max(s), s.index(x[, i[, j]]), s.count(x)
immutable sequence operations: hash()
mutable sequence operations: s[i:j:k] = t, del s[i:j:k], s.remove(x), s.reverse(), etc.
"""

# list: mutable
symbols = '$¢£¥€¤'
beyond_ascii = [162, 163, 165, 8364, 164]  # 1.square brackets
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]  # 2.list comprehension: impl by generator
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))  # 3.type constructor with iterable
beyond_ascii.sort(key=lambda n: n % 100, reverse=True)  # stable. to return new instance, use sorted(iterable)

# tuple: immutable
"""
a, or (a,)
a,b,c or (a,b,c)
tuple(iterable)
"""
divmod(20, 8)
divmod(*(20, 8))
a, *body, c, d = range(5)

# collections.namedtuple

City = collections.namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

LatLong = collections.namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
for key, value in delhi._asdict().items():
    print(key + ':', value)

# range: immutable

list(range(0, 30, 5))

# text sequence: str: immutable

''.join('{}'.format(i) for i in range(5))

# binary sequence: bytes: immutable

b'still allows embedded "double" quotes'  # ascii characters only
bytes(10)  # zero filled
bytes(range(20))  # by iterable

# binary sequence: bytearray: mutable version of bytes

# binary sequence: memoryview

v = memoryview(b'abcefg')
v[1]
bytes(v[1:4])

# set: mutable, unordered frozenset: immutable, unordered

{'jack', 'sjoerd'}
{s for s in ['jack', 'sjoerd']}
set(['jack', 'sjoerd'])
frozenset(['jack', 'sjoerd'])

# dict: mutable, unordered

m = {'one': 1, 'two': 2, 'three': 3}  # any hashable objects can be keys
m = dict(one=1, two=2, three=3)
m = dict([('two', 2), ('one', 1), ('three', 3)])
m = {k: v for k, v in [('two', 2), ('one', 1), ('three', 3)]}
m.keys(), m.values(), m.items()  # view objects

m.get('key', list())
m.setdefault('key', list()).append('value')
m = collections.defaultdict(list)

ct = collections.Counter('abracadabra')

# object https://docs.python.org/3.6/reference/datamodel.html#special-method-names
"""
new # e.g. override to support immutable 
init
(del)
repr # return a valid Python expression to recreate the object if possible
str: call repr
(bytes)
lt, le, ne, gt, ge: NotImplemented
eq: false if not self
hash: e.g. address. if override eq, return None.
bool: return len > 0 if defined len, otherwise return True.

getattr: called when an attribute lookup failed
getattribute: called unconditionally
setattr
delattr # should only be implemented if del obj.name is meaningful for the object
dir: called when dir(obj) is called

get, set, delete, set_name # for descriptor class, e.g dict

(slots): override to save space, since by default, instances of classes have a dictionary for attribute storage.

call

len, length_hint, getitem, missing, setitem, delitem, iter, reversed, contains

"""
# function
"""
decorators
- e.g. property, classmethod, staticmethod, functools.wraps, functools.lru_cache()
- run in import time.
- closures.
- stacked decorators.
- paramterized decorators.
"""
