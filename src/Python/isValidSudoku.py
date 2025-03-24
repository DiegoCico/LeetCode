class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue

                row_key = (val, 'row', i)
                col_key = (val, 'col', j)
                box_key = (val, 'box', i // 3, j // 3)

                if row_key in d or col_key in d or box_key in d:
                    return False

                d[row_key] = True
                d[col_key] = True
                d[box_key] = True

        return True
