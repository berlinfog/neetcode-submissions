class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows, cols, squs = set(), set(), set()
            for j in range(9):
                # 行检查
                val_r = board[i][j]
                if val_r != ".":
                    if val_r in rows: return False
                    rows.add(val_r)
                    
                # 列检查
                val_c = board[j][i]
                if val_c != ".":
                    if val_c in cols: return False
                    cols.add(val_c)
                    
                # 方格检查 (用你推导的 row_idx, col_idx)
                r, c = (i // 3) * 3 + (j // 3), (i % 3) * 3 + (j % 3)
                val_s = board[r][c]
                if val_s != ".":
                    if val_s in squs: return False
                    squs.add(val_s)              
        return True