class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix)
        row = len(matrix[0])
        l, r = 0, col*row - 1
        while l <= r:
            mid = (r - l)//2 + l
            temp = matrix[mid//row][mid%row]
            if temp == target:
                return True
            elif temp > target:
                r = mid - 1
            else:
                l = mid + 1
        return False