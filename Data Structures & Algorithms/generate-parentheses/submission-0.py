class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        def dfs(l,r,str1):
            if l + r == 2 * n:
                res.append(str1)
                return
            if l < n :
                dfs(l+1,r,str1+"(")
            if r < l :
                dfs(l,r+1,str1+")")


        dfs(0,0,"")
        return res