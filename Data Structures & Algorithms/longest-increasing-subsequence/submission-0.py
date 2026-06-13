class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # dp[i] means longest array end with i
        # dp[i] = dp[i-1] + 1 if nums[i] > nums[i-1] iterate and get max
        for i in range(1,n):
            tm = nums[i]
            for j in range(i):
                if tm > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)