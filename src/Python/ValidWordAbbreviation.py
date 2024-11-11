class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_length = len(word)
        j = 0  
        i = 0 
        
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                
                num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                
                j += num  
            else:
                if j >= word_length or word[j] != abbr[i]:
                    return False
                j += 1
                i += 1
        
        return j == word_length
