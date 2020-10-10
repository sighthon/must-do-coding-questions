# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/

from typing import List
from collections import OrderedDict, defaultdict


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def form_tree(arr: List):
    if not arr:
        return None

    root = TreeNode(arr.pop(0))
    stack = [root]
    while stack and arr:
        ele = stack.pop(0)
        if not ele:
            arr.pop(0)
            arr.pop(0)

        if arr:
            l = arr.pop(0)
            ele.left = TreeNode(l) if l else None
            stack.append(ele.left)
        if arr:
            r = arr.pop(0)
            ele.right = TreeNode(r) if r else None
            stack.append(ele.right)

    return root


def vertical_order(root: TreeNode):
    if not root:
        return []

    # last node based on horizontal distance
    ans = defaultdict(lambda : [])
    stack = [(root, 0)]  # (node, hor_dist)

    while stack:
        ele, hd = stack.pop(0)
        ans[hd].append(ele.value)

        if ele.left:
            stack.append((ele.left, hd-1))
        if ele.right:
            stack.append((ele.right, hd+1))

    ans = OrderedDict(sorted(ans.items()))
    return ans.values()


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, None, 9]]

    for a_ in a:
        root = form_tree(a_)
        print(vertical_order(root))
