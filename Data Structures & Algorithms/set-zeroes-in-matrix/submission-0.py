class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # lazy way is to iterate one time,mark the row and col number
        # and then if row and col number not in sepeate list
        # iterate second time to mark as zero
        # so maybe O(rows+cols) space is it O(1)

        r = len(matrix)
        c = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return
        