class Bag:
    def __init__(self, capacity):
        self.capacity = 50
        self.a = []
    def add(self, item):
        self.a.append(item)

b = Bag(50)
print(b.capacity)

b.add('nanoha')
b.add('sonico')
print(b.a)

print(id(b), type(b))   
"""
day 3 class 20min
thoughts
- really simple grammar, even without visibility 
"""
