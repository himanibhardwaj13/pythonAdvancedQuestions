# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import OrderedDict
class LRUClass:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
            self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to.end(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)

    
lru = LRUClass(2)
lru.put(1,"A")
lru.put(2,"B")
lru.put(3,"C")
result=  lru.get(1)
print(result)
