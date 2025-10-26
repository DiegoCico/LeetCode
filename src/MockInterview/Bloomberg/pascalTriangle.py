
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(arr[i-1][j-1] + arr[i-1][j])
            row.append(1)
            arr.append(row)
        return arr
