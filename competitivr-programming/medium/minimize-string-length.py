class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d = set()
        for i in s:
            d.add(i)
        return len(d)