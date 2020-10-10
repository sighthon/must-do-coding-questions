# 
from typing import List


def min_coins(coins: List, val: int):
    pass

if __name__ == "__main__":
    c = [[1, 5, 6, 9], [25,10,5]]
    v = [11, 30]

    for c_, v_ in zip(c, v):
        print(min_coins(c_, v_))
