class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = i
        res= []
        for j in range(len(nums)):
            if target - nums[j] in dict1 and j != dict1[target - nums[j]]:
                res.append(j)
                res.append(dict1[target - nums[j]])
                if res[0] > res[1]:
                    res[1],res[0] = res[0],res[1]
                return res