# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(root.right)

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print a.left
train = Solution()
train.invertTree(a)
print a.left
