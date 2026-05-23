class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l,r,t,b = 0,n-1,0,m-1
        res = []
        while l <= r and t <= b:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if t <= b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b -=1
            if l <= r:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l +=1
        return res
        