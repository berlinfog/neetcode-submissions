class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
        self.cache = {}

    def remove(self,node):
        pre,nex = node.prev,node.next
        pre.next,nex.prev = nex,pre
    
    def insert(self,node): # add at top
        pre,nex = self.left,self.left.next

        pre.next = node
        node.prev = pre

        nex.prev = node
        node.next = nex

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            pre = self.right.prev
            self.remove(pre)
            del self.cache[pre.key]