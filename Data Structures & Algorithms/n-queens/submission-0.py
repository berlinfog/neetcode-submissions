class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos = set()
        col = set()
        neg = set()
        res = []
        board = [['.'] * n for i in range(n)]
        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return
            for j in range(n):
                if j in col or i+j in pos or i-j in neg:
                    continue
                else:
                    board[i][j] = 'Q'
                    pos.add(i+j)
                    neg.add(i-j)
                    col.add(j)

                    dfs(i+1)

                    board[i][j] = '.'
                    pos.remove(i+j)
                    neg.remove(i-j)
                    col.remove(j)


        dfs(0)
        return res