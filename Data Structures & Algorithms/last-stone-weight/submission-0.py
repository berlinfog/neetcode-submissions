import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesn = [-x for x in stones]
        heapq.heapify(stonesn)
        while len(stonesn) > 1:
            stone1 = heapq.heappop(stonesn)
            stone2 = heapq.heappop(stonesn)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(stonesn,-abs(stone2-stone1))
        return 0 if len(stonesn) == 0 else -stonesn[0]