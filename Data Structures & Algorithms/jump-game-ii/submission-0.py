class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [n+1] * n 
        maxr = 0
        jumps[0] = 0
        for i in range(n):
            for j in range(i+1,min(i + nums[i] + 1, n)):
                jumps[j] = min(jumps[j],jumps[i]+1)
        return jumps[-1]

