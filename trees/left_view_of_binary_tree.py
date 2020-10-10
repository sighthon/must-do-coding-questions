# https://www.geeksforgeeks.org/print-left-view-binary-tree/

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


def print_left_view(root: TreeNode):
    # every first node in level order traversal
    stack = [(root, 0)]
    curr_lev = -1
    ans = []
    while stack:
        ele, lev = stack.pop(0)
        if lev != curr_lev:
            ans.append(ele.value)
            curr_lev = lev

        if ele.left:
            stack.append((ele.left, lev+1))
        if ele.right:
            stack.append((ele.right, lev+1))

    return ans


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        print(print_left_view(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)
    print(print_left_view(root))


