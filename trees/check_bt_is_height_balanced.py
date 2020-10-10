# https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

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

def check_height_balanced(root: TreeNode):
    if not root:
        return True

    l_height = height(root.left)
    r_height = height(root.right)

    return check_height_balanced(root.left) and \
        check_height_balanced(root.right) and \
            abs(l_height-r_height) <= 1

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        print(check_height_balanced(root))