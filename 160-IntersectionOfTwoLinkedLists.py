#T: O(A + B) / S: O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
      
# T: O(A + B) / S: O(A)  
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next
        
        while headB:
            if headB in setA: return headB
            else: headB = headB.next
        
        return None
