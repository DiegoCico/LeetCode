class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        curr_m = val
        if self.arr:
            curr_m = min(self.arr[-1][1], curr_m)
        return self.arr.append((val, curr_m))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()