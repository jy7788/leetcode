# Definition for a binary tree node.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index +=1
        for i in range(index,len(nums)):
            nums[i] = 0

train = Solution()
nums = [0,1,0,3,12]
train.moveZeroes(nums)
print nums
