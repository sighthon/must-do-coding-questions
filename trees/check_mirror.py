# https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/

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

def check_mirror(root_a: TreeNode, root_b: TreeNode):
    if not root_a and not root_b:
        return True

    if root_a and root_b:
        return root_a.value == root_b.value and \
            check_mirror(root_a.left, root_b.right) and \
                check_mirror(root_a.right, root_b.left)            
    
    return False

if __name__ == "__main__":
    a = [[1, 3, 2, None, None, 5, 4]]
    b = [[1, 2, 3, 4, 5, 6]]

    for a_, b_ in zip(a, b):
        root_a = form_tree(a_)
        root_b = form_tree(b_)
        print(check_mirror(root_a, root_b))