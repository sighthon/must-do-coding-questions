# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
# an easy answer is map

from typing import List


def pyth_triplet(arr: List):
    arr = [ele*ele for ele in list(set(arr))]  # storing the squares
    map_ = {ele: True for ele in arr}

    n = len(arr)
    for x in range(n):
        for y in range(x+1, n):
            if x + y in map_:
                return True

    return False


if __name__ == "__main__":
    a = [[3, 1, 4, 6, 5], [10, 4, 6, 12, 5]]

    for a_ in a:
        print(pyth_triplet(a_))
