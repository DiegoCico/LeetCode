class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minimun = len(nums)//3
        hm = defaultdict(list)
        res = []
        for i in nums:
            if i in hm:
                hm[i] += 1
            else: 
                hm[i] = 1

            if hm[i] > minimun and not i in res:
                res.append(i)
        return res
