from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxs = [[[0,0],[0,1],[0,2],
                [1,0],[1,1],[1,2],
                [2,0],[2,1],[2,2]],
         [[0,3],[0,4],[0,5],
                [1,3],[1,4],[1,5],
                [2,3],[2,4],[2,5]],
         [[0,6],[0,7],[0,8],
                [1,6],[1,7],[1,8],
                [2,6],[2,7],[2,8]]]
        col = defaultdict(set)
        row = defaultdict(set)
        i = 0
        while i < 3:
            k = 0
            while k < 3:
                p = set()
                for x in range(9):
                    if board[boxs[i][x][0]][boxs[i][x][1]] == ".":
                        boxs[i][x][0] += 3
                        continue
                    if board[boxs[i][x][0]][boxs[i][x][1]] in row[boxs[i][x][0]] or board[boxs[i][x][0]][boxs[i][x][1]] in col[boxs[i][x][1]] or board[boxs[i][x][0]][boxs[i][x][1]] in p:
                        return False
                    col[boxs[i][x][1]].add(board[boxs[i][x][0]][boxs[i][x][1]])
                    row[boxs[i][x][0]].add(board[boxs[i][x][0]][boxs[i][x][1]])
                    p.add(board[boxs[i][x][0]][boxs[i][x][1]])
                    boxs[i][x][0] += 3
                k += 1
            i += 1
        return True