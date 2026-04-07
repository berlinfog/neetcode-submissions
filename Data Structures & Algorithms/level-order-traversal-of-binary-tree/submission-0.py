# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # 边界处理
            return []
        lst = deque()
        lst.append(root)
        res = []

        while lst:
            temp = []
            lens = len(lst)
            for i in range(lens):
                node = lst.popleft()
                temp.append(node.val)
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)
            res.append(temp[:])
        return res
                
