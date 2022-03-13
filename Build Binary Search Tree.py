class Node:
    def __init__(self, val= 0, left = None, right= None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def add(self, root: Node, val: int):
        if root is None:
            return Node(val)
        if root.val < val:
            root.right = self.add(root.right, val)
        else:
            root.left = self.add(root.left, val)
        return root

    # recursive
    def inorder(self, root: Node):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    # iterative
    def inorderIter(self, root: Node):
        out = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if type(curr) is int:
                out.append(curr)
                continue
            if curr is not None:
                stack.append(curr.right)
                stack.append(curr.val)
                stack.append(curr.left)
        return out


s = Solution()

root = Node(50)
root = s.add(root, 30)
root = s.add(root, 70)
root = s.add(root, 20)
root = s.add(root, 40)
root = s.add(root, 60)
root = s.add(root, 80)

print(s.inorder(root))

print(s.inorderIter(root))
