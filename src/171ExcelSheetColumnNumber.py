# Definition for a binary tree node.
class Solution(object):
    def titleToNumber(self, s):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        re = 0
        for i in range(0,len(s)):
            re = re*26+ord(s[i])-64
        return re


train = Solution()
s = "AA"
print train.titleToNumber(s)
