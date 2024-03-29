#T: O(n) - One Pass, S: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        
        for _ in range(n):
            fast = fast.next
        print(fast.val)
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return dummy.next
        
            
