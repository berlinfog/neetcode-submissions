class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != 'O':
                return
            if board[i][j] =='O':
                board[i][j] = 'T'
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)

        for i in range(row):
            if  board[i][0] == 'O':
                dfs(i,0)
            if  board[i][col-1] == 'O':                
                dfs(i,col-1)
        for i in range(1,col-1):
            if  board[0][i] == 'O':
                dfs(0,i)
            if  board[row-1][i] == 'O':
                dfs(row-1,i)
        # 3. 遍历整个矩阵，进行最后的大洗牌
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    # 没被标记为 T 的 O，说明是被死死包围的孤岛，无情同化！
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # 之前顺藤摸瓜标记的逃生通道 T，现在安全了，恢复原貌！
                    board[r][c] = 'O'
