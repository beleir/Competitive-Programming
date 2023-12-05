class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"] 
        ans = []
        for i in words:
            row = 0
            broken = False
            for ro in range(1,3):
                if i[0].lower() in rows[ro]:
                    row = ro
                    break
            for x in i:
                if x.lower() not in rows[row]:
                    broken = True
                    break
            if not broken:
                ans.append(i)
        return ans