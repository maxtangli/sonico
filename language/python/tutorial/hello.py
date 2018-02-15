# hello
print("hello, python.")

# list
a = [1,2,3]
print(a)

#class range(stop)
#class range(start, stop[, step])
b = range(1,4)
print(list(b))

# lambda
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

squares = list(map(lambda x: x**2, range(1,10)))
print(squares)

# list comprehension
print([x**2 for x in range(1,10)])

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# tuple
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(u)

# set
a = set('abca')
b = set('bcdb')
print([a, b, a - b, a | b, a & b, a ^ b])

# dict
tel = {'jack': 4098, 'sape': 4139}
print(tel.keys())
for k,v in tel.items(): print(k,v)

"""
day 1: 80min
thoughts
- powerful data structures, lambda, list comprehensions
- brief coding style, though ruby is better 
- php is too old, c++ ?...
"""
# module
def hello():
    print("hello")

# generators, iterators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):print(char)
