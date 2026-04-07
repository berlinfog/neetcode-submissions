# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        p1 = 1 # 代表当前是第几位（1, 10, 100...）
        while l1:
            num1 += l1.val * p1
            p1 *= 10
            l1 = l1.next
            
        num2 = 0
        p2 = 1
        while l2:
            num2 += l2.val * p2
            p2 *= 10
            l2 = l2.next
            
        num3 = num1 + num2
        
        # 将结果转为字符串，并直接反转（因为我们要返回的也是个位在前）
        s = str(num3)[::-1]
        
        # 建立链表
        dummy = ListNode(0)
        curr = dummy
        for char in s:
            curr.next = ListNode(int(char))
            curr = curr.next
            
        return dummy.next
