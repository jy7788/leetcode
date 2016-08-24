# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSameTree(self, p,q):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        #print "%s,%s" % (p.val,q.val)
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(7)
a.left = b
a.right = c
d.left = e
d.right = f
train = Solution()
print train.isSameTree(a,d)
