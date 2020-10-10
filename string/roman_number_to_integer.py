# https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

from typing import List


def roman_to_integer(s: str):
    map_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ans = map_[s[0]]
    for idx in range(1, len(s)):
        if map_[s[idx-1]] < map_[s[idx]]:
            ans -= map_[s[idx-1]]
            ans += (map_[s[idx]] - map_[s[idx-1]])
        else:
            ans += map_[s[idx]]

    return ans


if __name__ == "__main__":
    a = ["IX", "XL", "MCMIV", "MMMCMXCIX"]

    for a_ in a:
        print(roman_to_integer(a_))
