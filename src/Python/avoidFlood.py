class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        out = [-1]*n
        next_rain = dict()
        predict = [-1]*n
        for i in range(n-1, -1, -1):
            x = rains[i]
            if x in next_rain:
                predict[i] = next_rain[x]
            next_rain[x] = i
        pq = []
        for i, x in enumerate(rains):
            if pq and pq[0] < i:
                return []
            if x==0:
                out[i] = rains[heappop(pq)] if pq else 1
            elif predict[i] != -1:
                heappush(pq, predict[i])
        return [] if pq else out