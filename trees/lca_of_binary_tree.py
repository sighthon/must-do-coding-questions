# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# The idea is to traverse the tree starting from root. 
# If any of the given keys (n1 and n2) matches with root, 
# then root is LCA (assuming that both keys are present). 
# If root doesn’t match with any of the keys, we recur for 
# left and right subtree. The node which has one key present 
# in its left subtree and the other key present in right subtree
#  is the LCA. If both keys lie in left subtree, then left subtree 
#  has LCA also, otherwise LCA lies in right subtree.

from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None


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

def lca(root: TreeNode, v1: int, v2: int):
    # every first node in level order traversal
    stack = [(root, 0)]
    n1 = None
    n2 = None

    while stack:
        ele, lev = stack.pop(0)

        if ele.value == v1:
            n1 = ele
        elif ele.value == v2:
            n2 = ele

        if ele.left:
            ele.left.parent = ele
            stack.append((ele.left, lev+1))
        if ele.right:
            ele.right.parent = ele
            stack.append((ele.right, lev+1))

    if not n1 or not n2:
        return None

    # track the parent
    if n1.parent and n1.parent == n2:
        return n2.value
    elif n2.parent and n2.parent == n1:
        return n1.value

    while n1.parent and n2.parent and n1.parent != n2.parent:
        n1 = n1.parent
        n2 = n2.parent

    if not n1.parent:
        return root.value
    return n1.parent.value

def lca_recursive(root: TreeNode, v1: int, v2: int):
    if not root:
        return None

    if root.value in [v1,v2]:
        return root
    
    left_lca = lca_recursive(root.left, v1, v2)
    right_lca = lca_recursive(root.right, v1, v2)
    
    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca else right_lca

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, 6, 7]]

    for a_ in a:
        root = form_tree(a_)
        # print(lca(root, 3, 4))
        # print(lca(root, 4,5))
        # print(lca(root, 4,6))
        # print(lca(root, 3,4))
        # print(lca(root, 2,4))

        print(lca_recursive(root, 3, 4).value)
        print(lca_recursive(root, 4,5).value)
        print(lca_recursive(root, 4,6).value)
        print(lca_recursive(root, 3,4).value)
        print(lca_recursive(root, 2,4).value)