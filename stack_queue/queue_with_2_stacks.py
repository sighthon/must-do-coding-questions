# https://www.geeksforgeeks.org/queue-using-stacks/

from typing import List


class Q:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, data):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        if self.s1:
            reurn self.s1.pop()
        return None
