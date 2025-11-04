class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ways = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    ways += 1
        return ways
