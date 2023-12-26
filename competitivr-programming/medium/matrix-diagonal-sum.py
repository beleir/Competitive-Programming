class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        r = {0:0,n-1:0}
        for i in range(n):
            for x in range(n):
                if i-x == 0:
                    r[0] += mat[i][x]
                elif i+x == n-1:
                    r[n-1] += mat[i][x]
        if n==1:
            return r[0]
        return r[0]+r[n-1]