class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # 哨兵节点
        cur = dummy
        carry = 0
        
        # 只要 l1, l2 没走完，或者还有进位，就继续
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # 计算总和及进位
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            
            # 建立新节点
            cur.next = ListNode(val)
            
            # 指针移动
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next