# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

from typing import List, Tuple
from functools import total_ordering
import operator


@total_ordering
class Timing:
    def __init__(self, a: Tuple, b: Tuple):
        self.start = a
        self.end = b

    def __str__(self):
        print(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start

    def __lt__(self, other):
        return self.start < other.start


def min_platforms(arr_a: List, arr_b: List):
    timings = [Timing(a, b) for a, b in zip(arr_a, arr_b)]
    timings.sort()

    print([timing.start for timing in timings])
    print([timing.end for timing in timings])

    trains = [timings[0]]
    for idx in range(1, len(timings)):
        s = timings[idx].start
        e = timings[idx].end

        if trains[-1].start <= s <= trains[-1].end:
            s = min(trains[-1].start, s)
            e = max(trains[-1].end, e)
            trains[-1] = Timing(s, e)
        else:
            trains.append(timings[idx])

    print([timing.start for timing in trains])
    print([timing.end for timing in trains])

    ans = len(timings) - len(trains)
    return ans if ans else 1


if __name__ == "__main__":
    a = [[(9, 0), (9, 40), (9, 50), (11, 0), (15, 0), (18, 0)], [(9,0), (9,40)]]
    b = [[(9, 10), (12, 0), (11, 20), (11, 30), (19, 0), (20, 0)], [(9,10), (12,00)]]

    for a_, b_ in zip(a, b):
        print(min_platforms(a_, b_))
