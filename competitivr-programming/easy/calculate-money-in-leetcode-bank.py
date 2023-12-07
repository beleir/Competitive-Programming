class Solution:
    def totalMoney(self, n: int) -> int:
        d = n//7
        e = n%7
        
        i = 1
        j = 0
        saved = 0
        while j < d:
            saved += (7/2)*(i+(7+i-1))
            i += 1
            j += 1
        saved += (e/2)*(i+e+i-1)
        return int(saved)