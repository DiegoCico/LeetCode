class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        for i in range(1, numRows):
            curr = []
            prev = triangle[i-1]
            curr.append(1) 
            
            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            
            curr.append(1)
            triangle.append(curr)
        return triangle