class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i >= j:
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(n):
                if j < n/2:
                    matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        return 