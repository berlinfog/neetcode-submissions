class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for k,i in enumerate(nums):
            dif = target - i
            if dif in maps:
                return [maps[dif],k]
            maps[i] = k