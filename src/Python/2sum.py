class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums[i+1:]:
                j = nums[i+1:].index(diff) + (i + 1)
                return[i, j]
        
        return -1