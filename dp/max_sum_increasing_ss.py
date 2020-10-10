# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
# variation of lis

from typing import List


def max_sum_increasing_ss(arr: List):
    n = len(arr)
    ans = [0]*n
    ans[0] = arr[0]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                ans[i] = max(ans[i], arr[i]+ans[j])     
        # print(ans)
    return max(ans)

if __name__ == "__main__":
    a = [[1, 101, 2, 3, 100, 4, 5],
    [3, 4, 5, 10],
    [10, 5, 4, 3]]

    for a_ in a:
        print(max_sum_increasing_ss(a_))
