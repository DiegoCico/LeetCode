class MaxStack:
    def __init__(self):
        self.stack = []      # normal stack
        self.max_stack = []  # track current max

    def push(self, x: int) -> None:
        # push value and current max
        cur_max = x if not self.max_stack else max(x, self.max_stack[-1])
        self.stack.append(x)
        self.max_stack.append(cur_max)

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer = []

        # pop until we find the top-most max
        while self.top() != max_val:
            buffer.append(self.pop())

        # remove that max
        self.pop()

        # push back the other elements
        while buffer:
            self.push(buffer.pop())

        return max_val
