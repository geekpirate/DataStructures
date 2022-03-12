class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def PostOrderTraversal(self, root: Node):
        return self.PostOrderTraversal(root.left) + self.PostOrderTraversal(root.right) + [root.val] if root else []


root = Node(1)
root.left = Node(5)
root.right = Node(6)
temp = root.left
temp.left = Node(3)
temp.right = Node(4)
temp = root.right
temp.right = Node(5)


s = Solution()
print(s.PostOrderTraversal(root))

