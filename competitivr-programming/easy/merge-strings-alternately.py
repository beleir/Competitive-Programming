class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = ""
        v = 0
        r = 0
        for i in range(len(word1)+len(word2)):
            if v >= len(word1):
                words += word2[r:]
                break
            if r >= len(word2):
                words += word1[v:]
                break
            elif i%2==0:
                words += word1[v]
                v += 1
            else:
                words += word2[r]
                r += 1
        return words