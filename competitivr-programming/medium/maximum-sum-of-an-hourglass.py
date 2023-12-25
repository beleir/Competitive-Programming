class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        finalsum = 0
        h = [0,2]
        while h[0] < len(grid)-2:
            b = (h[0]+2,h[1])
            su = 0
            v = 0
            r = 0
            bn = grid[h[0]+1][h[1]-1]
            st  = 0
            while st <= h[1]:
                v += grid[h[0]][st]
                r += grid[b[0]][st]
                st += 1
            su = max(su,r+bn+v)
            js = 1
            p = 0 
            while js < len(grid[0])-2:
                v -= grid[h[0]][p]
                r -= grid[h[0]+2][p]
                v += grid[h[0]][h[1]+p+1]
                r += grid[h[0]+2][h[1]+p+1]
                bn = grid[h[0]+1][h[1]+p]
                su = max(su,r+bn+v)
                p += 1
                js += 1
            finalsum = max(finalsum,su)
            h[0]+=1
        return finalsum