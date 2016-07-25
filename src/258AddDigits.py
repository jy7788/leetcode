class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num ==0:
			return 0;
		tmp = num%9
		if tmp == 0:
			return 9
		else:
			return tmp
a = Solution()
print a.addDigits(9)
