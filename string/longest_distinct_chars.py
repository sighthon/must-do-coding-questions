# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

from typing import List


def longest_dist_char_ss(s: str):
    map_ = {}

    n = len(s)
    ans = 0
    s_idx = 0
    e_idx = 0
    while e_idx < n:
        # print(s_idx, e_idx, map_)
        if s[e_idx] not in map_:
            map_[s[e_idx]] = 1
            e_idx += 1
        else:
            while s[e_idx] in map_ and s_idx <= e_idx:
                del map_[s[s_idx]]
                s_idx += 1
        ans = max(ans, e_idx-s_idx)

    return ans


if __name__ == "__main__":
    a = ["ABDEFGABEF", "BBBB", "GEEKSFORGEEKS"]

    for a_ in a:
        print(longest_dist_char_ss(a_))
        # break
