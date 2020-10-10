# https://www.geeksforgeeks.org/stock-buy-sell/
# buy and then try to sell

from typing import List


def max_profit(arr: List):
    n = len(arr)
    if n < 2:
        return 0

    buy_idx = 0
    sell_idx = -1
    profit = 0
    for idx in range(n):
        # buy index updates only when we earn profit
        if sell_idx == -1 and arr[idx] > arr[buy_idx]:
            sell_idx = idx
        elif sell_idx != -1:
            if arr[idx] > arr[sell_idx]:
                sell_idx = idx
            else:
                profit += arr[sell_idx]-arr[buy_idx]
                buy_idx = idx
                sell_idx = -1

    if buy_idx != -1 and sell_idx != -1:
        profit += arr[sell_idx]-arr[buy_idx]

    return profit


if __name__ == "__main__":
    a = [[100, 180, 260, 310, 40, 535, 695]]

    for a_ in a:
        print(max_profit(a_))
