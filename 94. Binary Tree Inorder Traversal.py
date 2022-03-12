class Node:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def InOrderTraversal(self, root: Node):
        return self.InOrderTraversal(root.left) + [root.val] + self.InOrderTraversal(root.right) if root else []



root = Node(1)
root.left = Node(5)
root.right = Node(2)
temp = root.right
temp.left = Node(3)

s = Solution()
# print(root.val)
print(s.InOrderTraversal(root))


