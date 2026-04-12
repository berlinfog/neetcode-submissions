class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def dfs(i):
            if i == len(s):
                res.append(temp[:])
                return
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    temp.append(sub)
                    dfs(j+1)
                    temp.pop()

        dfs(0)
        return res