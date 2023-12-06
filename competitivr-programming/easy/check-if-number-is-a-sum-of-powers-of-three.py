import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        def is_perfect_cube(x):
            x = abs(x)
            return int(round(x ** (1. / 3))) ** 3 == x
        def helper(v):
            print(v,"v")
            if v < 0:
                return False
            if v == 0:
                return True
            if v == 2:
                return False
            print(243**(1./3))
            print (v**(1./3),"RRR")
            if is_perfect_cube(v):
                return True
            i = ((3**(int(math.log(v,3))+1)-1)/2)-v
            print(i,(3**(int(math.log(v,3))+1)-1)/2)
            return helper(i)
        return helper(n)
        """
        if n < 1:
            return True
        if n%3 > 1:
            return False
        return self.checkPowersOfThree(n//3)