class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        d = []
        for i in digits:
            s += str(i)
        s = str(int(s)+1)
        for k in s:
            d.append(int(k))
        return d