class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def dfs(i):
            res.append(temp[:])
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]: #前面的解法里有了
                    continue
                temp.append(nums[j])
                dfs(j+1)
                temp.pop()
        
        dfs(0)
                
            

        return res

# 1 1 2 
# 12