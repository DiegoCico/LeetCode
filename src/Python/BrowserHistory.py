class BrowserHistory:

    def __init__(self, homepage: str):
        self.b = [homepage]  
        self.f = []

    def visit(self, url: str) -> None:
        self.f.clear()      
        self.b.append(url)

    def back(self, steps: int) -> str:
        moves = min(steps, len(self.b) - 1)
        for _ in range(moves):
            self.f.append(self.b.pop())
        return self.b[-1]

    def forward(self, steps: int) -> str:
        moves = min(steps, len(self.f))
        for _ in range(moves):
            self.b.append(self.f.pop())
        return self.b[-1]
