class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 其实有点像什么 选择加号或者减号然后拼起来 这个前后的话···
        nums.sort()
        #dp的话这个状态转移方程 选true或者false的话好像也不太行 dp[i][0]就是这个选加号时候的 ？
        # dfs的话 就好像也没有说可以提前结束的办法 估计还是dp
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]