class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        listcon = []
        lens = len(position)
        for i in range(lens):
            # 依然存 [位置, 时间]
            listcon.append([position[i], (target - position[i]) / speed[i]])
        
        # 1. 关键改动：按位置从大到小排序（离终点最近的在最前面）
        listcon.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for p, time in listcon:
            # 2. 核心逻辑：
            # 如果当前车的时间比栈顶（它前面的车）的时间长
            # 说明它追不上前面的车，它自己会带头形成一个新车队
            if not stack or time > stack[-1]:
                stack.append(time)
            # 如果 time <= stack[-1]，说明它会追上前面的车队，直接忽略（不入栈）
        
        # 栈里剩下的每一个时间点，都代表一个独立的车队头
        return len(stack)