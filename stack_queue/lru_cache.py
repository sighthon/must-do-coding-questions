# https://www.geeksforgeeks.org/lru-cache-implementation/

from typing import List

class LRUCache:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.map_ = {} # to store the position

    def get(self, x):
        if not self.queue or x not in self.queue:
            self.set(x, True)
            return None
        self.queue.remove(x)
        self.queue.append(x)
        return self.map_.get(x)

    def set(self, x, y):
        # remove the LRUed item
        if len(self.queue) >= self.size:
            del self.map_[self.queue.pop(0)]
        self.map_[x] = y
        self.queue.append(x)
    

if __name__ == "__main__":
    lru = LRUCache(5)
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    for page in pages:
        print(page, lru.get(page))
    
