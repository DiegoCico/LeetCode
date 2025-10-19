class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]] 
        for i in nums:
            n = len(arr)
            for j in range(n):
                add = arr[j] + [i]
                arr.append(add)
        return arr 