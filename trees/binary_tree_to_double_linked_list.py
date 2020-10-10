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

def tree_to_double_ll_util(root: TreeNode):
    # tree to double ll util
    if not root:
        return None

    if root.left:
        left = tree_to_double_ll_util(root.left)
        while left.right:
            left = left.right
        left.right = root
        root.left = left

    if root.right:
        right = tree_to_double_ll_util(root.right)
        while right.left:
            right = right.left
        right.left = root
        root.right = right

    return root


def tree_to_double_ll(root: TreeNode):
    # order should be inorder traversal of tree
    if not root:
        return

    root = tree_to_double_ll_util(root)

    while root.left:
        root = root.left

    return root


if __name__ == "__main__":
    a = [[10, 12, 15, 25, 30, 36]]

    for a_ in a:
        root = form_tree(a_)
        root = tree_to_double_ll(root)
        while root:
            print(root.value)
            root = root.right

