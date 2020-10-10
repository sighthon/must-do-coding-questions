# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

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

def height(root: TreeNode):
    if not root:
        return 0

    return 1 + max(height(root.left), height(root.right))

def diameter(root: TreeNode):
    # max of left, right or path passing through root
    if not root:
        return 0

    l_height = height(root.left)
    r_height = height(root.right)

    l_diam = diameter(root.left)
    r_diam = diameter(root.right)

    return max(l_diam, r_diam, 1 + l_height + r_height)

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        print(diameter(root))