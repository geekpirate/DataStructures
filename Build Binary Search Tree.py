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
        pass


s = Solution()

root = Node(50)
root = s.add(root, 30)
root = s.add(root, 70)
root = s.add(root, 20)
root = s.add(root, 40)
root = s.add(root, 60)
root = s.add(root, 80)

print(s.inorder(root))

