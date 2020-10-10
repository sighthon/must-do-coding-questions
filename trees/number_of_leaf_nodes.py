# https://www.geeksforgeeks.org/write-a-c-program-to-get-count-of-leaf-nodes-in-a-binary-tree/


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


def count_leaf_nodes(root: TreeNode):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        print(count_leaf_nodes(root))
