class Solution:
    def reverseWords(self, s: str) -> str:
        j = list(s.split())
        out = ""
        for x in range(len(j)-1,-1,-1):
            if x == 0:
                out += j[x]
            else:
                out += j[x] + " "
            print(out,j[x])
        return out