import copy
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        ad = []
        for x in range(len(matrix[0])):
            for v in range(len(matrix)):
                ad.append(0)
            transpose.append(ad)
            ad = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transpose[j][i] = matrix[i][j]
        return transpose