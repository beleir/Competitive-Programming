class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        v = 0
        for x in s:
            if v >= len(g):
                break
            if x>=g[v]:
                v += 1
        return v