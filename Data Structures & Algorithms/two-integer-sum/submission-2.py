class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff],k]
            prevMap[v] = k