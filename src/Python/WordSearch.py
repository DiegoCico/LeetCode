def dfs(r, c, curr, word, board, visited):
    if not (0 <= r < len(board) and 0 <= c < len(board[0])) or (r, c) in visited:
        return False

    curr += board[r][c]

    if curr == word:
        return True
    if not word.startswith(curr):
        return False

    visited.add((r, c))
    found = (dfs(r+1, c, curr, word, board, visited) or
             dfs(r-1, c, curr, word, board, visited) or
             dfs(r, c+1, curr, word, board, visited) or
             dfs(r, c-1, curr, word, board, visited))
    visited.remove((r, c))
    return found


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    attempt = dfs(i, j, "", word, board, set())
                    if attempt:
                        return True
                    
        return False
        