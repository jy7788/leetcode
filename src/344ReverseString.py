class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rt = list(s)
        rt.reverse()
        re = "".join(rt)
        return re
a = Solution()
print a.reverseString("hello")
