# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 1. 让 right 先走 n 步
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 2. 左右指针一起走，直到 right 到底
        while right:
            left = left.next
            right = right.next
            
        # 3. 此时 left 在待删节点的前一个，执行删除
        left.next = left.next.next
        
        return dummy.next