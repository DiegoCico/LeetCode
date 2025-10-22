class HitCounter:

    def __init__(self):
        self.arr = defaultdict(list)

    def hit(self, timestamp: int) -> None:
        if timestamp in self.arr:
            self.arr[timestamp] += 1
        else:
            self.arr[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        low = 0 if (timestamp - 300) < 0 else (abs(timestamp-300) + 1)
        print(f"low {low}")
        summ = 0
        for t, h in self.arr.items():
            if t < low or t > timestamp:
                continue 
            print(f"t {t} : h {h}")
            summ += h
            print(f"sum {summ}")
        return summ
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)