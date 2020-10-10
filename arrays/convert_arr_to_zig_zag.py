# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
# sort and one pass bubble sort by keeping arr[0] intact

from typing import List


def zig_zag(arr: List):
    arr.sort()
    for idx in range(2, len(arr), 2):
        arr[idx-1], arr[idx] = arr[idx], arr[idx-1]

def zig_zag_without_sort(arr: List):
    curr_ope = "<"
    for idx in range(1, len(arr)):
        if (curr_ope == "<" and arr[idx-1] > arr[idx]) or \
            (curr_ope == ">" and arr[idx-1] < arr[idx]):
            arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
            
        curr_ope = ">" if curr_ope == "<" else "<"


if __name__ == "__main__":
    a = [[4, 3, 7, 8, 6, 2, 1], [1, 4, 3, 2]]

    for a_ in a:
        zig_zag_without_sort(a_)
        print(a_)
