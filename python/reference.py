# Built-in Functions
"""
math: abs(), all(), any(), ascii(), chr(), divmod(), hex(), max(), min(), oct(), ord(), pow(), round(), sum()
type: bool(), bin(), complex(), float(), int()
collection type: bytearray(), bytes(), dict(), enumerate(), frozenset(), list(), map(), memoryview(), range(), set(), str(), tuple()
collection operation: filter(), ?iter(), len(), next(), reversed(), slice(), sorted(), zip()
object: callable(), classmethod(), delattr(), getattr(), hasattr(), hash(), id(), isinstance(), issubclass(), object(), property(), repr(), setattr(), staticmethod(), super(), type(), vars()
io: format(), input(), open(), print()
language: compile(), dir(), eval(), exec(), globals(), help(), locals(), __import__()
"""

# Built-in Constants
"""
False,True,None,NotImplemented,Ellipsis,__debug__
"""

# object() todo

# list
symbols = '$¢£¥€¤'
beyond_ascii = [162, 163, 165, 8364, 164]  # 1.square brackets
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]  # 2.list comprehension: impl by generator
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))  # 3.type constructor with iterable

# tuple todo

# range todo

# iterable operations
"""
map(function, iterable) -> iterator
filter(function, iterable) -> iterator
reduce(function, iterable) -> value
"""
