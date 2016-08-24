# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0;
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return l+1 if l>r else r+1

a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(1)
d = TreeNode(1)
a.left = b
a.right = c
c.left = d
train = Solution()
print train.maxDepth(a)
