class Solution:
# 1 2 3 
# 0 - 213 312 
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = set()
        temp = nums
        def dfs(i,temp):
            if i == len(nums)-1:
                res.add(tuple(temp))
                return
            for j in range(i+1,len(nums)):
                temp[j],temp[i] = temp[i],temp[j]
                dfs(i+1,temp[:])
                temp[j],temp[i] = temp[i],temp[j]
                dfs(i+1,temp[:])
        
        dfs(0,nums)
        reslst = []
        for i in res:
            reslst.append(list(i))
        return reslst
                