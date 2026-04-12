class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])


        def dfs(i,j,c):
            if c == len(word):
                return True
            elif i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[c]:
                return False
            else:
                temp = board[i][j]
                board[i][j] = '#'
                res =  dfs(i,j+1,c+1) or dfs(i+1,j,c+1) or dfs(i,j-1,c+1) or dfs(i-1,j,c+1)
                board[i][j] = temp
                return res
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0) == True:
                    return True

        return False
