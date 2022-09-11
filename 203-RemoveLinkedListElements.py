class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = prev = dummy
        
        while cur:
            if cur.val == val:
                temp = cur
                prev.next = cur.next
                cur = prev.next
            else: 
                prev = cur
                cur = cur.next
        return dummy.next
