T: O(n), S: O(1)
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
    
    
# without dummy Node
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head
        
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = head.next
            else:
                prev = cur    
            cur = cur.next
            
        return head
