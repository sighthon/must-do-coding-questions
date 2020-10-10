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

def print_left_view(root: TreeNode):
    # every first node in level order traversal
    stack = [(root, 0)]
    nodes = []

    while stack:
        ele, lev = stack.pop(0)
        next_node_lev = -1 if not stack else stack[0][1]

        if ele:
            nodes.append(ele)

        if next_node_lev != lev:
            ele.right_next = None
        else:
            ele.right_next = stack[0][0]

        if ele.left:
            stack.append((ele.left, lev+1))
        if ele.right:
            stack.append((ele.right, lev+1))

    return nodes

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        print(print_left_view(root))