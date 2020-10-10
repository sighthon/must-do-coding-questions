# https://www.geeksforgeeks.org/queue-based-approach-for-first-non-repeating-character-in-a-stream/

from typing import List


def first_non_rep(arr: List):
    n = len(arr)
    ans = []
    que = []

    for ele in arr:
        if not que:
            que.append(ele)
            ans.append(ele)
        elif que and ele == que[0]:
            # pop all while they match to bring first non repeating to start
            while que and que[0] == ele:
                que.pop(0)
            if que:
                ans.append(que[0])
            else:
                ans.append(-1)
        else:
            ans.append(que[0])

    return ans


if __name__ == "__main__":
    a = [['a', 'a', 'b', 'c'], ['a', 'a', 'c']]

    for a_ in a:
        print(first_non_rep(a_))