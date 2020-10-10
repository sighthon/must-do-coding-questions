#

from typing import List


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


def is_bst(root: TreeNode, min_: int, max_: int):
    if not root or (not root.left and not root.right):
        return True
    if not min_ < root.value < max_:
        return False

    return is_bst(root.left, min_, min(root.value, max_)) and \
        is_bst(root.right, max(min_, root.value), max_)


if __name__ == "__main__":
    a = [[4, 2, 5, 1, 3]]
    INT_MAX = 10**10

    for a_ in a:
        root = form_tree(a_)
        print(is_bst(root, -INT_MAX, INT_MAX))
