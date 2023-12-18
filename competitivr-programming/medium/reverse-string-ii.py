class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def rever(n):
            return n[::-1]
        if 2*k > len(s) >= k:
            return rever(s[:k])+s[k:]
        outs = ""
        for i in range(0,len(s),2*k):
            if i + k >= len(s):
                outs += rever(s[i:])
                continue
            outs += rever(s[i:i+k])
            outs += s[i+k:i+2*k]
        return outs