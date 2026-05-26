class CountSquares:

    def __init__(self):
        self.sq = dict()

    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        if pt in self.sq:
            self.sq[pt] += 1
        else:
            self.sq[pt] = 1

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]
        res = 0
        
        # 直接遍历字典里所有已经存在的点 px, py
        for (px, py), count_p in self.sq.items():
            # 1. 检查 px, py 是否能和 qx, qy 构成正方形的对角线
            if abs(qx - px) != abs(qy - py) or qx == px:
                continue  # 不是对角线，或者距离为 0，直接跳过
                
            # 2. 另外两个点的坐标直接确定
            p1 = (px, qy)
            p2 = (qx, py)
            
            # 3. 如果另外两个点也都存在，直接把组合数乘起来加到结果里
            if p1 in self.sq and p2 in self.sq:
                res += count_p * self.sq[p1] * self.sq[p2]
                
        return res