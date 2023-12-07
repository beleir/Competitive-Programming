class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        def helper(i,n):
            if n == len(spaces):
                return s[i:]
            return s[i:spaces[n]] + " " + helper(spaces[n],n+1)
        return helper(0,0)