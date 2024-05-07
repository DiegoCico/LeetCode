class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        amount = max(candies)
        list = []
        for i in candies:
            if amount <= (i+extraCandies):
                list.append(True)
            else:
                list.append(False)
        return list
