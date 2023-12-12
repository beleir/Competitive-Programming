class Solution:
    def isHappy(self, n: int) -> bool:
        def help(n,vst):
            if n in vst:
                return False
            vst.add(n)
            j = 0
            for i in str(n):
                j += int(i)**2
            if j == 1:
                return True
            return help(j,vst)
        return help(n,set())