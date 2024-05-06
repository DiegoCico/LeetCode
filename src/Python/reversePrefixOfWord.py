class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        index = word.index(ch)

        l = list(word)

        left, right = 0, index
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        return ''.join(l)
