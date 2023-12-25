class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        j = {}
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if x+y not in j:
                    j[x+y] = [x+y, mat[x][y]]
                else:
                    j[x+y].append(mat[x][y])
        js = []
        for v in j:
            js.append(j[v])
        js.sort()
        outed = []
        for i in range(len(js)):
            if i%2:
                for xv in range(1,len(js[i])):
                    outed.append(js[i][xv])
            else:
                for vh in range(len(js[i])-1,0,-1):
                    outed.append(js[i][vh])
        return outed