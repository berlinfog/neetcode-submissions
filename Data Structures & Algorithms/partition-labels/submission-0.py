from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1. 记录每个字符最后出现的位置
        last_index = {char: i for i, char in enumerate(s)}
        
        res = []
        start, end = 0, 0
        
        # 2. 第二次遍历，滚动更新边界
        for i, char in enumerate(s):
            # 只要进来了，当前的区间终点至少要覆盖到当前字符的最后位置
            end = max(end, last_index[char])
            
            # 当指针追上了预设的终点，说明一个合法区间诞生了
            if i == end:
                res.append(end - start + 1)
                start = i + 1  # 下一个区间的起点
                
        return res