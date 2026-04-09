class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        def dfs(i,cur):
            if cur == target:
                res.append(temp[:])
                return
            elif cur > target:
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                temp.append(candidates[j])
                dfs(j+1,cur+candidates[j])
                temp.pop()

        dfs(0,0)
        return res
            