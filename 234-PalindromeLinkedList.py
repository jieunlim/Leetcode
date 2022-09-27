class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def recur(right):
            if right:
                recur(right.next)
                if right.val != self.left.val:
                    self.res = False
                self.left = self.left.next
                
            
            
        self.res = True
        self.left = head
        recur(head)
        
        return self.res
        


# O(n), O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head) -> bool:
        
        #876 find mid
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #206 reverse
        prev = None
     
        
        while slow:
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        #compare
        
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
                
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(1)

l1.next = l2
l2.next = l3

l1 = []
obj = Solution()
print(obj.isPalindrome(l1))

# 92. Reverse Linked List II
# 237. Delete Node in a Linked List
# 725. Split Linked List in Parts

# 379. Design Phone Directory
# 845. Longest Mountain in Array
# 977. Squares of a Sorted Array
