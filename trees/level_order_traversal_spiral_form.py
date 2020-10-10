# https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/

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


def level_order_spiral(root: TreeNode):
    if not root:
        return []

    # spiral traversal
    ans = []
    stack_rl = [root]  # (node, level)
    stack_lr = []
    while stack_lr or stack_rl:
        while stack_rl:
            ele = stack_rl.pop(-1)
            ans.append(ele.value)
            if ele.left:
                stack_lr.append(ele.left)
            if ele.right:
                stack_lr.append(ele.right)

        while stack_lr:
            ele = stack_lr.pop(0)
            ans.append(ele.value)
            if ele.left:
                stack_rl.append(ele.left)
            if ele.right:
                stack_rl.append(ele.right)

    return ans


if __name__ == "__main__":
    a = [[1, 2, 3, 7, 6, 5, 4]]

    for a_ in a:
        root = form_tree(a_)
        print(level_order_spiral(root))
