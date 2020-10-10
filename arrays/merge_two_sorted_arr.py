# https://www.geeksforgeeks.org/merge-two-sorted-arrays/

from typing import List


def merge_two_sorted_arr(arr_a: List, arr_b: List):
    # merge of merge sort
    a_idx = 0
    b_idx = 0
    ans = []

    while a_idx < len(arr_a) and b_idx < len(arr_b):
        if arr_a[a_idx] < arr_b[b_idx]:
            ans.append(arr_a[a_idx])
            a_idx += 1
        else:
            ans.append(arr_b[b_idx])
            b_idx += 1

    while a_idx < len(arr_a):
        ans.append(arr_a[a_idx])
        a_idx += 1

    while b_idx < len(arr_b):
        ans.append(arr_b[b_idx])
        b_idx += 1

    return ans


if __name__ == "__main__":
    a = [[1, 3, 4, 5], [5, 8, 9]]
    b = [[2, 4, 6, 8], [4, 7, 8]]
    for a_,b_ in zip(a, b):
        ans_ = merge_two_sorted_arr(a_, b_)
        print(ans_)
