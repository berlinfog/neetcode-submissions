from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = []
        for key,val in c.items():
            freq.append([-val,key])
        heapq.heapify(freq)
        res = []
        for i in range(k):
            res.append(heapq.heappop(freq)[1])
        return res

