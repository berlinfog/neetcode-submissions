class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # 左右两个虚拟哨兵节点，方便插入和删除，不用判断 None
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # 辅助函数：从链表中移除一个节点
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # 辅助函数：在最左侧（MRU位置）插入一个节点
    def insert(self, node):
        prev, nxt = self.left, self.left.next
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # 只要访问了，就先移除再插到最前面
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果已存在，先删掉旧的
            self.remove(self.cache[key])
        
        # 创建新节点并存入哈希表
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # 如果超量，删除最久未使用的（靠近 right 哨兵的节点）
        if len(self.cache) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]