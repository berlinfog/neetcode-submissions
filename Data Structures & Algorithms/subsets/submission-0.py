class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subnet = []
        def dfs(num):
            if num >= len(nums):
                res.append(subnet[:])
                return
            subnet.append(nums[num])
            dfs(num+1)

            subnet.pop()
            dfs(num+1)
        dfs(0)
        return res
