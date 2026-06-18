class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if (sums + target)%2 == 1:
            return 0
        val = (sums + target)//2
        dp = [0 for _ in range(val+1)]
        dp[0] = 1
        for num in nums:
            for i in range(val,num-1,-1):
                dp[i] += dp[i-num]
        return dp[val]