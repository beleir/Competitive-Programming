from collections import defaultdict
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        place = defaultdict(int)
        j = len(matrix)
        for i in range(j):
            for k in range(j):
                place[(k,j-1-i)] = matrix[i][k]
        for x in range(j):
            for y in range(j):
                matrix[x][y] = place[(x,y)]    