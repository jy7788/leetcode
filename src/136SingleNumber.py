# Definition for a binary tree node.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        result = 0
        for i in range(0,len(nums)):
            result ^=nums[i]
        return result


train = Solution()
nums = [1,2,3,3,2]
print train.singleNumber(nums)
