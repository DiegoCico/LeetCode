# O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            highest = i if i > 0 else 0
            lowest = i+1 if i+1 < len(nums) else len(nums)

            prefix = math.prod(nums[0:highest])
            suffix = math.prod(nums[lowest:len(nums)])
            res.append((prefix*suffix))
        return res
    
# O(n)
class Solution:
    # Define a method that takes a list of integers and returns a list of integers
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: get how many numbers there are
        n = len(nums)

        # Step 2: create a result array filled with 1s (same length as nums)
        res = [1] * n

        # Step 3: compute prefix products (product of all elements before index i)
        prefix = 1                     # start prefix as 1 (no elements before first)
        for i in range(n):
            res[i] = prefix            # store current prefix product in res[i]
            prefix *= nums[i]          # multiply prefix by current element for next step

        # Step 4: compute suffix products (product of all elements after index i)
        suffix = 1                     # start suffix as 1 (no elements after last)
        for i in range(n - 1, -1, -1): # iterate backward
            res[i] *= suffix           # multiply stored prefix with suffix product
            suffix *= nums[i]          # update suffix by multiplying current element

        # Step 5: return final result
        return res
