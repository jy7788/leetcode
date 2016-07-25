class Solution(object):
	def intersection(self, nums1,nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: bool
		"""
		result = list()
		tmp = set(nums1)
		tmp_ = list(set(nums2))
		for num in tmp_:
			if num in tmp:
				result.append(num)
		return result
a = Solution()
print a.intersection(9)
