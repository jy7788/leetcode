# Definition for a binary tree node.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type root: ListNode
        :rtype: TreeNode
        """
        if node == None:
            return
        node.val = node.next.val
        node.next = node.next.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(2)
f = ListNode(7)
a.next = b
b.next = c
c.next = d
train = Solution()
train.deleteNode(c)
index = a
while index != None:
    print index.val
    index = index.next
