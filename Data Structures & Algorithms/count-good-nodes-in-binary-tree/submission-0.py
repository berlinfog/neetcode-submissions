# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def comNodes(root,value):
            if not root:
                return 0
            if root.val >= value:
                value = root.val
                return 1 + comNodes(root.left,value) + comNodes(root.right,value)
            else:
                return comNodes(root.left,value) + comNodes(root.right,value)
        return comNodes(root,root.val)