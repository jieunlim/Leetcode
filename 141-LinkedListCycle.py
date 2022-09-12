class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# s: o(1)
# t: o(n)
# https://leetcode.com/problems/linked-list-cycle/discuss/44539/AC-Python-76ms-Floyd-loop-detection-in-7-lines
# Floyd's Cycle Detection Alogrithm or Tortoise and Hare Algorithm
class Solution:
    def hasCycle(self, head):
        
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow. next 
            
            if fast == slow:
                return True
       
        return False
    
    

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow = head
        fast = head.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow == fast: return True
        if not fast : return False
        
        
        
        
    def hasCycle2(self, head):
        #s: o(n)
        #t: o(n)
        s = set()
        while head and head.next:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
        
head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

head.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

obj = Solution()
print(obj.hasCycle(head))
