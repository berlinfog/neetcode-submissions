# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root]) # 还是用我们熟悉的 deque
        
        while queue:
            level_len = len(queue)
            
            for i in range(level_len):
                node = queue.popleft()
                
                # 💡 核心逻辑：如果是这一层的最后一个节点，就说明它是从右边能看到的
                if i == level_len - 1:
                    res.append(node.val)
                
                # 正常的 BFS 入队顺序：先左后右
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res