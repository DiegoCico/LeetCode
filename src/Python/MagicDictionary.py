class MagicDictionary:

    def __init__(self):
        self.data = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.data = dictionary

    def search(self, searchWord: str) -> bool:
        for i in self.data:
            if len(i) != len(searchWord):
                continue
            c = 0
            for j in range(len(i)):
                if i[j] != searchWord[j]:
                    c +=1
            if c == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)