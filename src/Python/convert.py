class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        l = [[] for _ in range(numRows)]
        counter = 0
        going_down = True

        for i in s:
            l[counter].append(i)

            if counter == 0:
                going_down = True
            elif counter == numRows - 1:
                going_down = False

            counter = counter + 1 if going_down else counter - 1

        return ''.join(char for row in l for char in row)
