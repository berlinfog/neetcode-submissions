import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointr = points[:]
        for i in range(len(points)):
            points[i] = [points[i][0]* points[i][0]+points[i][1]*points[i][1],i]
        heapq.heapify(points)
        res = []
        for i in range(k):
            res.append(pointr[heapq.heappop(points)[1]])
        return res
        