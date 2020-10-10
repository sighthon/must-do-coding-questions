# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/
# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space

from typing import List


def rearrange(arr: List):
    if not arr:
        return None

    n = len(arr)
    ans = [-1]*n
    num_even_pos = n // 2

    arr_idx = 0
    idx = 1
    while arr_idx < num_even_pos and idx < n:
        ans[idx] = arr[arr_idx]
        idx += 2
        arr_idx += 1

    arr_idx = n-1
    idx = 0
    while arr_idx >= num_even_pos and idx < n:
        ans[idx] = arr[arr_idx]
        idx += 2
        arr_idx -= 1

    return ans


def rearrange_rec(arr: List, idx: int, pos_seen: List):
    if not arr:
        return

    # s_idx = idx*2 + 1
    # l_idx = (n-1-idx)*2

    if idx in pos_seen:
        return 

    n = len(arr)
    even_pos = n // 2
    val = arr[idx]
    pos_seen.append(idx)

    if idx < even_pos:
        to_idx = idx*2 + 1
    else:
        to_idx = (n-1-idx)*2
    rearrange_o1(arr, to_idx, pos_seen)
    arr[to_idx] = val

    return arr

def rearrange_o1(arr: List):
    if not arr:
        return

    n = len(arr)
    min_idx = 0
    max_idx = n-1
    max_ele = arr[max_idx] + 1

    for idx in range(n):
        if idx % 2 == 0:
            arr[idx] += arr[max_idx] % max_ele * max_ele
            max_idx -= 1
        else:
            arr[idx] += arr[min_idx] % max_ele * max_ele
            min_idx += 1


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6]]

    for a_ in a:
        # ans_ = rearrange(a_)
        # print(ans_)

        # pos_seen = []
        # for idx in range(len(a_)//2):
        #     rearrange_rec(a_, idx, pos_seen)
        # print(a_)
        
        org_max = max(a_) + 1
        rearrange_o1(a_)
        print([ele//org_max for ele in a_])
        
