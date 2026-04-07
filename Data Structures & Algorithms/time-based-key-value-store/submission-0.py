import collections

class TimeMap:
    def __init__(self):
        # 使用 defaultdict(list) 方便自动初始化 key 对应的列表
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 直接追加，因为题目保证了 timestamp 是递增的
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # 二分查找：寻找满足 val_timestamp <= timestamp 的最大值
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                # 找到了一个可能的过去版本，记录它并尝试向右找更近的
                res = values[m][1]
                l = m + 1
            else:
                # 这个版本太新了，往左找
                r = m - 1
        return res