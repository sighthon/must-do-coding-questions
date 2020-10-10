# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/

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


def serialise(root: TreeNode, ans: List):
    # pre order
    if not root:
        ans.append(-1)
        return

    ans.append(root.value)
    serialise(root.left, ans)
    serialise(root.right, ans)


idx = 0


def deserialize(arr: List):
    global idx
    if arr[idx] == -1:
        idx += 1
        return None

    node = TreeNode(arr[idx])
    idx += 1
    node.left = deserialize(arr)
    node.right = deserialize(arr)

    return node


if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5, None, 6]]

    for a_ in a:
        root = form_tree(a_)
        ans = []
        serialise(root, ans)
        print(ans)
        root = deserialize(ans)

        ans = []
        serialise(root, ans)
        print(ans)

