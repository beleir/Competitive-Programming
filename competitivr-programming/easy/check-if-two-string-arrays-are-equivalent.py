class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wor1 = ""
        wor2 = ""
        for i in word1:
            wor1 += i
        for j in word2:
            wor2 += j
        return wor1 == wor2