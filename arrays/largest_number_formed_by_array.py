# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

from typing import List

def compare(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (int(ba) > int(ab)) - (int(ba) < int(ab))

def myCompare(cmp):
    class K(object): 
        def __init__(self, obj, *args): 
            self.obj = obj 
        def __lt__(self, other): 
            return compare(self.obj, other.obj) < 0
        def __gt__(self, other): 
            return compare(self.obj, other.obj) > 0
        def __eq__(self, other): 
            return compare(self.obj, other.obj) == 0
        def __le__(self, other): 
            return compare(self.obj, other.obj) <= 0
        def __ge__(self, other): 
            return compare(self.obj, other.obj) >= 0
        def __ne__(self, other): 
            return compare(self.obj, other.obj) != 0
    return K

def largest_number_formed(arr: List):
    # group numbers together by prepending them at start or end
    # arr.sort(key=lambda x: compare(x))
    arr = sorted(arr, key=myCompare(compare))
    print(arr)
    ans = "".join([str(i) for i in arr])
    return ans


if __name__ == "__main__":
    a = [[54, 546, 548, 60], [1, 34, 3, 98, 9, 76, 45, 4]]

    for a_ in a:
        print(largest_number_formed(a_))
