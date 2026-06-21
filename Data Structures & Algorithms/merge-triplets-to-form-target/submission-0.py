class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 讲道理应该有个什么lambda 排序 根据 triplets 0 1 2 来 从小到大 然后for 从小到大 merge 
        # 如果发现小的那个1或2超了的话就给他去掉 
        sat = set()
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            for j in range(3):
                if i[j] == target[j]:
                    sat.add(j)
            if len(sat) == 3:
                return True
        return len(sat) == 3