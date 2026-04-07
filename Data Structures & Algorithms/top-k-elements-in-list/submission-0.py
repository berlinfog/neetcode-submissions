from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = Counter(nums)
        lst = []
        res = []
        for key,val in cont.items():
            lst.append([-val,key])
        heapq.heapify(lst)
        for i in range(k):
            res.append(heapq.heappop(lst)[1])
        return res