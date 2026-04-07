class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        lens = len(nums)
        for i in range(len(nums)):
           l,r = i+1,lens-1
           while l < r:
            if nums[l]+nums[r] + nums[i] == 0:
                res.append(tuple([nums[i],nums[l],nums[r]]))
                l += 1
                r -= 1
            elif nums[l]+nums[r] + nums[i] > 0:
                r -= 1
            else:
                l += 1
        return list(set(res))