# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

from typing import List


class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack:
            self.min_stack.append(data)
        else:
            self.min_stack.append(min(self.min_stack[-1], data))

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None


class SpecialStackO1ExtraSpace:
    def __init__(self):
        self.stack = []
        self.min_ele = 10**10

    def push(self, data):
        if not self.stack or data >= self.min_ele:
            self.stack.append(data)
        else:
            self.stack.append(2*data - self.min_ele)

        self.min_ele = min(self.min_ele, data)

    def pop(self):
        if not self.stack:
            return None
        ele = self.stack.pop()
        if ele < self.min_ele:
            self.min_ele = 2*self.min_ele - ele
        return ele

    def getMin(self):
        return self.min_ele if self.stack else None


if __name__ == "__main__":
    a = [16, 15, 29, 19, 18]
    ss = SpecialStackO1ExtraSpace()
    for ele in a:
        ss.push(ele)
        print(ss.getMin())
