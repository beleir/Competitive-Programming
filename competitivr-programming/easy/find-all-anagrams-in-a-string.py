class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)> len(s):
            return []
        d = defaultdict(int)
        chk = defaultdict(int)
        out = []
        for x in p:
            chk[x] += 1
        for i in range(len(p)):
            d[s[i]] += 1
        if d == chk:
            out.append(0)
        for x in range(len(p),len(s)):
            d[s[x]] += 1
            d[s[x-len(p)]] -= 1
            if d[s[x-len(p)]] == 0:
                d.pop(s[x-len(p)])
            if d==chk :
                out.append(x-len(p)+1)
        return out