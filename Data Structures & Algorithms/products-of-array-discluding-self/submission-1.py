class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        l = 1
        r = 1
        right = []
        for i in nums:
            l *= i
            left.append(l)
        for i in nums[::-1]:
            r *= i
            right.append(r)
        right = right[::-1]
        res = []
        lenn = len(nums)
        for i in range(lenn):
            res.append((1 if i < 1 else left[i-1]) * (1 if i >= lenn-1 else right[i+1]))
        return res
