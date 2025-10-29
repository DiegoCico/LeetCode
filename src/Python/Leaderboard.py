class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.board[playerId] += score
        else:
            self.board[playerId] = score

    def top(self, K: int) -> int:
        scores = []
        for p, s in self.board.items():
            scores.append(s)
        
        scores.sort()

        return sum(scores[-K:])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0 


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)