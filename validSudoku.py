# https://leetcode.com/problems/valid-sudoku/?envType=study-plan&id=data-structure-i

class Solution:
    def isSafe(self,l,board):
        for sub in l:
            d = {}
            row,col = sub[0],sub[1]
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j] != '.' and board[i][j] in d:
                        d[board[i][j]]+=1
                    else:
                        d[board[i][j]] = 1
            for ct in d:
                if d[ct]>1:
                    return False
        return True
    
    def isValidSudoku(self, board):
        l = [[0,0],[3,0],[6,0],[0,3],[3,3],[3,6],[0,6],[6,6],[6,3]]
        
        if not self.isSafe(l, board):
            return False
        
        for i in range(9):
        
            for j in range(9):
                digit = board[i][j]
                ctDig = 0
            

                for row in range(9):
                    if digit!='.' and digit == board[i][row]:
                        ctDig+=1
                        if ctDig>=2:
                            return False 
                ctDig = 0
                for col in range(9):
                    if digit!='.' and digit == board[col][j]:
                        ctDig+=1
                        # print(digit,board[col][j])
                        if ctDig>=2:
                            return False
        return True

board = [[".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","3","4",".",".",".","."]
,[".",".",".",".",".","3",".",".","."]
,[".",".",".",".",".","5","2",".","."]]

# board = [[".",".",".",".","5",".",".","1","."]
# ,[".","4",".","3",".",".",".",".","."]
# ,[".",".",".",".",".","3",".",".","1"]
# ,["8",".",".",".",".",".",".","2","."]
# ,[".",".","2",".","7",".",".",".","."]
# ,[".","1","5",".",".",".",".",".","."]
# ,[".",".",".",".",".","2",".",".","."]
# ,[".","2",".","9",".",".",".",".","."]
# ,[".",".","4",".",".",".",".",".","."]]

# for i in range(9):
#     for j in range(9):
#         print(board[i][j],end='  ')
#     print()

s = Solution()
print(s.isValidSudoku(board))
