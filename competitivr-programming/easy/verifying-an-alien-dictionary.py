class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            for x in range(len(words[i])):
                if x >= len(words[i+1]):
                    return False
                if order.index(words[i][x])<order.index(words[i+1][x]):
                    break
                if order.index(words[i][x])>order.index(words[i+1][x]):
                    return False
        return True