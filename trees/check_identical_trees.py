# https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/

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

def check_identical_trees(root_a: TreeNode, root_b: TreeNode):
    # every first node in level order traversal
    stack_a = [root_a]
    stack_b = [root_b]

    while stack_a and stack_b:
        ele_a = stack_a.pop(0)
        ele_b = stack_b.pop(0)
        if ele_a.value != ele_b.value:
            return False

        if ele_a.left:
            stack_a.append(ele_a.left)
        if ele_a.right:
            stack_a.append(ele_a.right)

        if ele_b.left:
            stack_b.append(ele_b.left)
        if ele_b.right:
            stack_b.append(ele_b.right)

    if stack_a or stack_b:
        return False

    return True

def check_identical_trees_rec(root_a: TreeNode, root_b: TreeNode):
    if not root_a and not root_b:
        return True

    if root_a and root_b:
        return root_a.value == root_b.value and \
            check_identical_trees_rec(root_a.left, root_b.left) and \
                check_identical_trees_rec(root_a.right, root_b.right)            
    
    return False

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]
    b = [[1, 2, 3, 4, 5, None, 6]]

    for a_, b_ in zip(a, b):
        root_a = form_tree(a_)
        root_b = form_tree(b_)
        # print(check_identical_trees(root_a, root_b))
        print(check_identical_trees_rec(root_a, root_b))