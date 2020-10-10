# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

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

def max_path_sum_util(root: TreeNode):
    if not root:
        return 0

    l_path = max_path_sum_util(root.left)
    r_path = max_path_sum_util(root.right)

    max_single = max(max(l_path, r_path) + root.value, root.value)
    max_top = max(max_single, l_path+r_path+root.value)

    max_path_sum_util.res = max(max_top, max_path_sum_util.res)

    return max_single


def max_path_sum(root: TreeNode):
    if not root:
        return 0

    max_path_sum_util.res = -10**10
    max_path_sum_util(root)

    return max_path_sum_util.res


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6], [1,2,3], [10, 2, 10, 20, 1, None, -25]]

    for a_ in a:
        root = form_tree(a_)
        print(max_path_sum(root))