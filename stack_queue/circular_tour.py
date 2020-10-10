# https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/

from typing import List


def circular_tour(pet: List, dist: List):
    n = len(pet)
    s_idx = 0
    e_idx = 1
    curr_pet = pet[0] - dist[0]

    while e_idx != s_idx or curr_pet < 0:
        while curr_pet < 0 and s_idx != e_idx:
            curr_pet -= pet[s_idx] - dist[s_idx]
            s_idx = (s_idx+1) % n

            if s_idx == 0:
                return -1

        curr_pet += pet[e_idx] - dist[e_idx]
        e_idx = (e_idx+1) % n

    return s_idx


if __name__ == "__main__":
    a = [[4, 6, 7, 4]]
    b = [[6, 5, 3, 5]]

    for a_, b_ in zip(a, b):
        print(circular_tour(a_, b_))
