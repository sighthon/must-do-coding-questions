# https://www.geeksforgeeks.org/find-subarray-with-given-sum

from typing import List


def sub_array_sum(arr: List, sum_: int):
    if not arr:
        return None, None

    s_idx = 0
    c_sum = arr[0]
    n = len(arr)
    e_idx = 1

    while e_idx < n:
        if c_sum == sum_:
            return s_idx, e_idx-1

        c_sum += arr[e_idx]

        # remove from start
        while s_idx < e_idx and c_sum > sum_:
            # print(s_idx, e_idx)
            c_sum -= arr[s_idx]
            s_idx += 1

        e_idx += 1

    return -1, -1


if __name__ == "__main__":
    a = [[1, 4, 20, 3, 10, 5], [1, 4, 0, 0, 3, 10, 5], [1, 4]]
    s = [33, 7, 0]

    for a_, s_ in zip(a, s):
        st, en = sub_array_sum(a_, s_)
        print(st, en)
