class Solution:
    def mergeAlternately(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        counter1 = 0
        counter2 = 0
        merge = ""

        while counter1 < length1 or counter2 < length2:
            if counter1 < length1:
                merge += word1[counter1]
                counter1+=1
            if counter2 < length2:
                merge += word2[counter2]
                counter2+=1

        return merge
            