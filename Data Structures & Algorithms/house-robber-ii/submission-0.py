class Solution:
    def rob(self, nums: List[int]) -> int:
        # 💡 特殊情况防坑：如果只有 1 栋房子，直接抢它，不然下面的切片会切出空数组
        if len(nums) == 1:
            return nums[0]

        # 封装刚刚写好的 O(1) 打劫神技
        def helper(arr):
            prev2, prev1 = 0, 0
            for n in arr:
                curr = max(n + prev2, prev1)
                prev2, prev1 = prev1, curr
            return prev1

        # 两次循环（两个平行宇宙大比拼）
        # 方案 A：抢头不抢尾（切片去掉最后一个）
        ans1 = helper(nums[:-1])
        # 方案 B：抢尾不抢头（切片去掉第一个）
        ans2 = helper(nums[1:])

        # 谁赚得多听谁的
        return max(ans1, ans2)